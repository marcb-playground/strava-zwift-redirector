# webhook_handler.py
from flask import jsonify

from strava_utils import fetch_activity_detail, move_activity_to_user
from garmin_utils import sync_activity_to_garmin


def process_strava_activity(data, source_client, target_client, garmin_client, wattage_threshold):
    if not data:
        raise RuntimeError('No data received')

    activity_id = data.get('object_id')
    if not activity_id:
        raise RuntimeError('No activity ID provided')

    try:
        activity = fetch_activity_detail(source_client, activity_id)
    except RuntimeError as e:
        raise RuntimeError(str(e)) from e

    activity_name = getattr(activity, 'name', '') or ''

    if activity.average_watts < wattage_threshold:
        moved_activity_id = move_activity_to_user(
            source_client=source_client,
            source_activity_id=activity_id,
            target_client=target_client,
            wattage_threshold=wattage_threshold,
        )
        if moved_activity_id is not None:
            return {
                'message': 'Activity moved to target',
                'activity_id': moved_activity_id,
            }, 200
        return {
            'message': 'No action taken for activity',
            'activity_id': activity_id,
        }, 200

    if 'mywhoosh' in activity_name.lower():
        output_path = f'/tmp/strava_activity_{activity_id}'
        result = sync_activity_to_garmin(
            source_client=source_client,
            garmin_client=garmin_client,
            activity_id=activity_id,
            output_path=output_path,
            activity_name=activity_name,
            manufacturer=1,
            product=1836,
            activity_type='indoorride',
            require_fit=True,
        )
        return {
            'message': 'Activity routed to Garmin',
            'activity_id': activity_id,
            'result': result,
        }, 200

    return {
        'message': 'No action taken for activity',
        'activity_id': activity_id,
    }, 200


def handle_strava_notification(data, source_client, target_client, garmin_client, wattage_threshold):
    payload, status = process_strava_activity(
        data=data,
        source_client=source_client,
        target_client=target_client,
        garmin_client=garmin_client,
        wattage_threshold=wattage_threshold,
    )
    return jsonify(payload), status

