import pytest
import xml.etree.ElementTree as ET
from xml_utils import move_watts_to_power
TMP_ROOT_FOLDER = "/tmp/"
@pytest.fixture
def gpx_file():
    # Create a temporary GPX file for testing
    gpx_content = '''<?xml version="1.0" encoding="UTF-8"?>
<gpx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd" creator="StravaGPX" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/v1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3">
 <metadata>
  <time>2024-09-12T12:04:29Z</time>
 </metadata>
 <trk>
  <name>Zwift - Loch Loop in Scotland</name>
  <type>VirtualRide</type>
  <trkseg>
   <trkpt lat="55.6420510" lon="-5.2394130">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>29</gpxtpx:watts>
      <gpxtpx:cad>58</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6420400" lon="-5.2394160">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>32</gpxtpx:watts>
      <gpxtpx:cad>60</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6420290" lon="-5.2394190">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>35</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6420180" lon="-5.2394210">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>36</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6420020" lon="-5.2394250">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>37</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6419860" lon="-5.2394280">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>36</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6419590" lon="-5.2394310">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>37</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6419430" lon="-5.2394350">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>40</gpxtpx:watts>
      <gpxtpx:cad>68</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6419220" lon="-5.2394390">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>40</gpxtpx:watts>
      <gpxtpx:cad>69</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6418950" lon="-5.2394430">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>43</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6418680" lon="-5.2394470">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>45</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6418410" lon="-5.2394520">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>45</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6418140" lon="-5.2394570">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6417820" lon="-5.2394640">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6417500" lon="-5.2394730">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6417180" lon="-5.2394830">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6416800" lon="-5.2394950">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6416480" lon="-5.2395090">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6416160" lon="-5.2395250">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6415780" lon="-5.2395410">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6415360" lon="-5.2395590">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6414980" lon="-5.2395770">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6414600" lon="-5.2395950">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6414230" lon="-5.2396140">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413800" lon="-5.2396320">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413370" lon="-5.2396510">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6412990" lon="-5.2396710">
    <ele>53.6</ele>
    <time>2024-09-12T12:04:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6412620" lon="-5.2396900">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6412140" lon="-5.2397090">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6411710" lon="-5.2397290">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6411280" lon="-5.2397470">
    <ele>53.8</ele>
    <time>2024-09-12T12:04:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6410850" lon="-5.2397660">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6410420" lon="-5.2397840">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6409940" lon="-5.2398020">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6409510" lon="-5.2398200">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6409030" lon="-5.2398430">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6408650" lon="-5.2398760">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6408220" lon="-5.2399190">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6407850" lon="-5.2399740">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6407520" lon="-5.2400390">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6407310" lon="-5.2401140">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6407150" lon="-5.2401980">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6407040" lon="-5.2402850">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6407040" lon="-5.2403720">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6406880" lon="-5.2404570">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6406660" lon="-5.2405370">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6406400" lon="-5.2406080">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6406020" lon="-5.2406640">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6405540" lon="-5.2407050">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6405060" lon="-5.2407300">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>49</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6404570" lon="-5.2407380">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>49</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6404040" lon="-5.2407310">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>49</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6403550" lon="-5.2407050">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6403070" lon="-5.2406630">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6402700" lon="-5.2406070">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6402370" lon="-5.2405380">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6402110" lon="-5.2404630">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6401780" lon="-5.2403920">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6401350" lon="-5.2403420">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6400870" lon="-5.2403070">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6400330" lon="-5.2402840">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6399850" lon="-5.2402710">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6399320" lon="-5.2402630">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6398780" lon="-5.2402580">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6398300" lon="-5.2402530">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6397760" lon="-5.2402520">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6397220" lon="-5.2402570">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6396740" lon="-5.2402660">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6396200" lon="-5.2402780">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6395720" lon="-5.2402900">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6395180" lon="-5.2403020">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6394650" lon="-5.2403140">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6394170" lon="-5.2403230">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6393630" lon="-5.2403300">
    <ele>53.8</ele>
    <time>2024-09-12T12:05:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6393090" lon="-5.2403330">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6392560" lon="-5.2403350">
    <ele>53.6</ele>
    <time>2024-09-12T12:05:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6392020" lon="-5.2403360">
    <ele>53.4</ele>
    <time>2024-09-12T12:05:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6391380" lon="-5.2403380">
    <ele>53.2</ele>
    <time>2024-09-12T12:05:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6390840" lon="-5.2403380">
    <ele>53.2</ele>
    <time>2024-09-12T12:05:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6390140" lon="-5.2403350">
    <ele>53.0</ele>
    <time>2024-09-12T12:05:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6389550" lon="-5.2403230">
    <ele>52.8</ele>
    <time>2024-09-12T12:05:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6388910" lon="-5.2403010">
    <ele>52.6</ele>
    <time>2024-09-12T12:05:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6388210" lon="-5.2402660">
    <ele>52.4</ele>
    <time>2024-09-12T12:05:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6387570" lon="-5.2402240">
    <ele>52.2</ele>
    <time>2024-09-12T12:05:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6386920" lon="-5.2401760">
    <ele>52.0</ele>
    <time>2024-09-12T12:05:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6386280" lon="-5.2401190">
    <ele>52.0</ele>
    <time>2024-09-12T12:05:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385640" lon="-5.2400550">
    <ele>51.8</ele>
    <time>2024-09-12T12:05:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6384990" lon="-5.2399780">
    <ele>51.4</ele>
    <time>2024-09-12T12:05:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6384350" lon="-5.2398960">
    <ele>51.2</ele>
    <time>2024-09-12T12:05:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383760" lon="-5.2398050">
    <ele>50.8</ele>
    <time>2024-09-12T12:05:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383170" lon="-5.2396990">
    <ele>50.4</ele>
    <time>2024-09-12T12:05:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382850" lon="-5.2395600">
    <ele>50.2</ele>
    <time>2024-09-12T12:06:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382850" lon="-5.2394080">
    <ele>50.0</ele>
    <time>2024-09-12T12:06:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382900" lon="-5.2392570">
    <ele>49.8</ele>
    <time>2024-09-12T12:06:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382850" lon="-5.2391040">
    <ele>49.6</ele>
    <time>2024-09-12T12:06:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382630" lon="-5.2389520">
    <ele>49.4</ele>
    <time>2024-09-12T12:06:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382360" lon="-5.2388040">
    <ele>49.0</ele>
    <time>2024-09-12T12:06:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6381880" lon="-5.2386650">
    <ele>48.8</ele>
    <time>2024-09-12T12:06:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6381400" lon="-5.2385340">
    <ele>48.6</ele>
    <time>2024-09-12T12:06:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6380810" lon="-5.2384100">
    <ele>48.2</ele>
    <time>2024-09-12T12:06:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6380220" lon="-5.2382920">
    <ele>48.0</ele>
    <time>2024-09-12T12:06:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6379520" lon="-5.2381790">
    <ele>47.8</ele>
    <time>2024-09-12T12:06:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6378820" lon="-5.2380730">
    <ele>47.6</ele>
    <time>2024-09-12T12:06:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6378070" lon="-5.2379720">
    <ele>47.2</ele>
    <time>2024-09-12T12:06:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6377320" lon="-5.2378790">
    <ele>47.0</ele>
    <time>2024-09-12T12:06:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6376460" lon="-5.2377930">
    <ele>46.8</ele>
    <time>2024-09-12T12:06:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6375600" lon="-5.2377140">
    <ele>46.6</ele>
    <time>2024-09-12T12:06:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374800" lon="-5.2376440">
    <ele>46.4</ele>
    <time>2024-09-12T12:06:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6373890" lon="-5.2375820">
    <ele>46.2</ele>
    <time>2024-09-12T12:06:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372980" lon="-5.2375280">
    <ele>46.0</ele>
    <time>2024-09-12T12:06:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372120" lon="-5.2374830">
    <ele>45.8</ele>
    <time>2024-09-12T12:06:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6371210" lon="-5.2374470">
    <ele>45.6</ele>
    <time>2024-09-12T12:06:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6370240" lon="-5.2374210">
    <ele>45.4</ele>
    <time>2024-09-12T12:06:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6369330" lon="-5.2374030">
    <ele>45.2</ele>
    <time>2024-09-12T12:06:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6368360" lon="-5.2373940">
    <ele>45.2</ele>
    <time>2024-09-12T12:06:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6367450" lon="-5.2373950">
    <ele>45.0</ele>
    <time>2024-09-12T12:06:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6366540" lon="-5.2374030">
    <ele>44.8</ele>
    <time>2024-09-12T12:06:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365630" lon="-5.2374200">
    <ele>44.8</ele>
    <time>2024-09-12T12:06:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6364720" lon="-5.2374440">
    <ele>44.6</ele>
    <time>2024-09-12T12:06:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6363860" lon="-5.2374510">
    <ele>44.4</ele>
    <time>2024-09-12T12:06:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6362940" lon="-5.2374120">
    <ele>44.2</ele>
    <time>2024-09-12T12:06:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6362190" lon="-5.2373220">
    <ele>44.0</ele>
    <time>2024-09-12T12:06:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361660" lon="-5.2371910">
    <ele>43.6</ele>
    <time>2024-09-12T12:06:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361230" lon="-5.2370420">
    <ele>43.4</ele>
    <time>2024-09-12T12:06:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361010" lon="-5.2368810">
    <ele>43.0</ele>
    <time>2024-09-12T12:06:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6360850" lon="-5.2367160">
    <ele>42.8</ele>
    <time>2024-09-12T12:06:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6360800" lon="-5.2365470">
    <ele>42.4</ele>
    <time>2024-09-12T12:06:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6360800" lon="-5.2363780">
    <ele>42.2</ele>
    <time>2024-09-12T12:06:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6360800" lon="-5.2362070">
    <ele>42.0</ele>
    <time>2024-09-12T12:06:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6360850" lon="-5.2360350">
    <ele>41.6</ele>
    <time>2024-09-12T12:06:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6360960" lon="-5.2358650">
    <ele>41.4</ele>
    <time>2024-09-12T12:06:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361010" lon="-5.2356930">
    <ele>41.2</ele>
    <time>2024-09-12T12:06:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361120" lon="-5.2355210">
    <ele>41.0</ele>
    <time>2024-09-12T12:06:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361230" lon="-5.2353500">
    <ele>40.6</ele>
    <time>2024-09-12T12:06:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361390" lon="-5.2351790">
    <ele>40.6</ele>
    <time>2024-09-12T12:06:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361500" lon="-5.2350100">
    <ele>40.4</ele>
    <time>2024-09-12T12:06:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361660" lon="-5.2348410">
    <ele>40.2</ele>
    <time>2024-09-12T12:06:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6361870" lon="-5.2346760">
    <ele>40.2</ele>
    <time>2024-09-12T12:06:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6362090" lon="-5.2345130">
    <ele>40.0</ele>
    <time>2024-09-12T12:06:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6362410" lon="-5.2343570">
    <ele>39.8</ele>
    <time>2024-09-12T12:06:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6362840" lon="-5.2342130">
    <ele>39.8</ele>
    <time>2024-09-12T12:06:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6363370" lon="-5.2340770">
    <ele>39.6</ele>
    <time>2024-09-12T12:06:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6364020" lon="-5.2339660">
    <ele>39.6</ele>
    <time>2024-09-12T12:06:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6364820" lon="-5.2338840">
    <ele>39.4</ele>
    <time>2024-09-12T12:06:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365680" lon="-5.2338340">
    <ele>39.4</ele>
    <time>2024-09-12T12:06:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6366540" lon="-5.2338180">
    <ele>39.2</ele>
    <time>2024-09-12T12:06:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6367450" lon="-5.2338250">
    <ele>39.2</ele>
    <time>2024-09-12T12:06:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6368360" lon="-5.2338390">
    <ele>39.0</ele>
    <time>2024-09-12T12:06:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6369220" lon="-5.2338510">
    <ele>39.0</ele>
    <time>2024-09-12T12:06:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6370080" lon="-5.2338630">
    <ele>38.8</ele>
    <time>2024-09-12T12:06:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6370990" lon="-5.2338710">
    <ele>38.8</ele>
    <time>2024-09-12T12:06:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6371800" lon="-5.2338760">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372710" lon="-5.2338760">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6373510" lon="-5.2338710">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374370" lon="-5.2338580">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6375230" lon="-5.2338400">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6376030" lon="-5.2338140">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6376790" lon="-5.2337850">
    <ele>38.8</ele>
    <time>2024-09-12T12:07:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6377590" lon="-5.2337550">
    <ele>38.8</ele>
    <time>2024-09-12T12:07:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6378290" lon="-5.2337270">
    <ele>39.0</ele>
    <time>2024-09-12T12:07:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6379040" lon="-5.2337030">
    <ele>39.0</ele>
    <time>2024-09-12T12:07:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6379740" lon="-5.2336860">
    <ele>39.2</ele>
    <time>2024-09-12T12:07:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6380430" lon="-5.2336760">
    <ele>39.2</ele>
    <time>2024-09-12T12:07:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6381130" lon="-5.2336700">
    <ele>39.4</ele>
    <time>2024-09-12T12:07:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6381830" lon="-5.2336670">
    <ele>39.4</ele>
    <time>2024-09-12T12:07:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382470" lon="-5.2336600">
    <ele>39.4</ele>
    <time>2024-09-12T12:07:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383120" lon="-5.2336390">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383710" lon="-5.2336050">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6384300" lon="-5.2335560">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6384830" lon="-5.2334930">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385260" lon="-5.2334170">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385690" lon="-5.2333240">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385900" lon="-5.2332250">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6386120" lon="-5.2331190">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6386170" lon="-5.2330090">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6386170" lon="-5.2328990">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6386120" lon="-5.2327870">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6386010" lon="-5.2326800">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385800" lon="-5.2325760">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385580" lon="-5.2324720">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385310" lon="-5.2323740">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385050" lon="-5.2322780">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6384780" lon="-5.2321830">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6384460" lon="-5.2320870">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6384190" lon="-5.2319940">
    <ele>39.6</ele>
    <time>2024-09-12T12:07:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383810" lon="-5.2319020">
    <ele>39.4</ele>
    <time>2024-09-12T12:07:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383440" lon="-5.2318120">
    <ele>39.4</ele>
    <time>2024-09-12T12:07:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383010" lon="-5.2317260">
    <ele>39.2</ele>
    <time>2024-09-12T12:07:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382580" lon="-5.2316480">
    <ele>39.2</ele>
    <time>2024-09-12T12:07:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382040" lon="-5.2315790">
    <ele>39.0</ele>
    <time>2024-09-12T12:07:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6381450" lon="-5.2315230">
    <ele>38.8</ele>
    <time>2024-09-12T12:07:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6380750" lon="-5.2314850">
    <ele>38.8</ele>
    <time>2024-09-12T12:07:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6380110" lon="-5.2314650">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6379410" lon="-5.2314610">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6378660" lon="-5.2314720">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6378020" lon="-5.2314900">
    <ele>38.6</ele>
    <time>2024-09-12T12:07:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6377320" lon="-5.2315050">
    <ele>38.4</ele>
    <time>2024-09-12T12:07:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6376570" lon="-5.2315070">
    <ele>38.4</ele>
    <time>2024-09-12T12:07:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6375870" lon="-5.2314900">
    <ele>38.4</ele>
    <time>2024-09-12T12:07:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6375230" lon="-5.2314420">
    <ele>38.2</ele>
    <time>2024-09-12T12:07:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374750" lon="-5.2313560">
    <ele>38.2</ele>
    <time>2024-09-12T12:07:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374420" lon="-5.2312430">
    <ele>38.0</ele>
    <time>2024-09-12T12:07:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374260" lon="-5.2311180">
    <ele>37.8</ele>
    <time>2024-09-12T12:07:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374160" lon="-5.2309900">
    <ele>37.6</ele>
    <time>2024-09-12T12:07:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374100" lon="-5.2308590">
    <ele>37.6</ele>
    <time>2024-09-12T12:07:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374000" lon="-5.2307280">
    <ele>37.4</ele>
    <time>2024-09-12T12:07:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6373780" lon="-5.2306010">
    <ele>37.2</ele>
    <time>2024-09-12T12:07:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6373350" lon="-5.2304890">
    <ele>37.0</ele>
    <time>2024-09-12T12:07:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372710" lon="-5.2304110">
    <ele>36.8</ele>
    <time>2024-09-12T12:07:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6371960" lon="-5.2303740">
    <ele>36.6</ele>
    <time>2024-09-12T12:07:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6371210" lon="-5.2303880">
    <ele>36.4</ele>
    <time>2024-09-12T12:07:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6370460" lon="-5.2304410">
    <ele>36.4</ele>
    <time>2024-09-12T12:08:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6369760" lon="-5.2305070">
    <ele>36.2</ele>
    <time>2024-09-12T12:08:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6369010" lon="-5.2305670">
    <ele>36.0</ele>
    <time>2024-09-12T12:08:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6368260" lon="-5.2305890">
    <ele>36.0</ele>
    <time>2024-09-12T12:08:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6367450" lon="-5.2305580">
    <ele>35.8</ele>
    <time>2024-09-12T12:08:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6366810" lon="-5.2304950">
    <ele>35.8</ele>
    <time>2024-09-12T12:08:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6366160" lon="-5.2304030">
    <ele>35.8</ele>
    <time>2024-09-12T12:08:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365730" lon="-5.2302930">
    <ele>35.8</ele>
    <time>2024-09-12T12:08:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365360" lon="-5.2301710">
    <ele>35.8</ele>
    <time>2024-09-12T12:08:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365200" lon="-5.2300430">
    <ele>36.0</ele>
    <time>2024-09-12T12:08:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365040" lon="-5.2299160">
    <ele>36.0</ele>
    <time>2024-09-12T12:08:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>49</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6364980" lon="-5.2297930">
    <ele>36.2</ele>
    <time>2024-09-12T12:08:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>48</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6364930" lon="-5.2296710">
    <ele>36.2</ele>
    <time>2024-09-12T12:08:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>48</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6364980" lon="-5.2295540">
    <ele>36.4</ele>
    <time>2024-09-12T12:08:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365040" lon="-5.2294410">
    <ele>36.6</ele>
    <time>2024-09-12T12:08:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365090" lon="-5.2293330">
    <ele>36.8</ele>
    <time>2024-09-12T12:08:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365140" lon="-5.2292290">
    <ele>37.0</ele>
    <time>2024-09-12T12:08:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365200" lon="-5.2291280">
    <ele>37.0</ele>
    <time>2024-09-12T12:08:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365310" lon="-5.2290310">
    <ele>37.2</ele>
    <time>2024-09-12T12:08:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365310" lon="-5.2289370">
    <ele>37.4</ele>
    <time>2024-09-12T12:08:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365410" lon="-5.2288470">
    <ele>37.4</ele>
    <time>2024-09-12T12:08:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365470" lon="-5.2287590">
    <ele>37.6</ele>
    <time>2024-09-12T12:08:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365570" lon="-5.2286740">
    <ele>37.8</ele>
    <time>2024-09-12T12:08:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365630" lon="-5.2285930">
    <ele>37.8</ele>
    <time>2024-09-12T12:08:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365730" lon="-5.2285130">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365840" lon="-5.2284360">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6365950" lon="-5.2283610">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6366110" lon="-5.2282870">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6366320" lon="-5.2282160">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6366540" lon="-5.2281470">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6366810" lon="-5.2280790">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6367130" lon="-5.2280140">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6367450" lon="-5.2279510">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6367770" lon="-5.2278880">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6368090" lon="-5.2278280">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6368470" lon="-5.2277700">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6368850" lon="-5.2277110">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6369220" lon="-5.2276500">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6369540" lon="-5.2275920">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6369970" lon="-5.2275300">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6370350" lon="-5.2274680">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6370720" lon="-5.2274020">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6371050" lon="-5.2273340">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6371420" lon="-5.2272610">
    <ele>38.0</ele>
    <time>2024-09-12T12:08:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6371740" lon="-5.2271830">
    <ele>37.8</ele>
    <time>2024-09-12T12:08:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372010" lon="-5.2270980">
    <ele>37.8</ele>
    <time>2024-09-12T12:08:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372230" lon="-5.2270060">
    <ele>37.8</ele>
    <time>2024-09-12T12:08:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372440" lon="-5.2269150">
    <ele>37.8</ele>
    <time>2024-09-12T12:08:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372600" lon="-5.2268200">
    <ele>37.8</ele>
    <time>2024-09-12T12:08:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6372820" lon="-5.2267240">
    <ele>37.8</ele>
    <time>2024-09-12T12:08:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6373080" lon="-5.2266310">
    <ele>37.6</ele>
    <time>2024-09-12T12:08:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6373410" lon="-5.2265450">
    <ele>37.6</ele>
    <time>2024-09-12T12:08:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6373780" lon="-5.2264650">
    <ele>37.4</ele>
    <time>2024-09-12T12:08:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374260" lon="-5.2263870">
    <ele>37.4</ele>
    <time>2024-09-12T12:08:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6374690" lon="-5.2263110">
    <ele>37.2</ele>
    <time>2024-09-12T12:08:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6375230" lon="-5.2262360">
    <ele>37.0</ele>
    <time>2024-09-12T12:08:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6375710" lon="-5.2261590">
    <ele>37.0</ele>
    <time>2024-09-12T12:08:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6376250" lon="-5.2260850">
    <ele>36.8</ele>
    <time>2024-09-12T12:08:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6376790" lon="-5.2260120">
    <ele>36.8</ele>
    <time>2024-09-12T12:08:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6377320" lon="-5.2259400">
    <ele>36.6</ele>
    <time>2024-09-12T12:08:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6377910" lon="-5.2258690">
    <ele>36.6</ele>
    <time>2024-09-12T12:09:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6378500" lon="-5.2257980">
    <ele>36.4</ele>
    <time>2024-09-12T12:09:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6379040" lon="-5.2257250">
    <ele>36.4</ele>
    <time>2024-09-12T12:09:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6379630" lon="-5.2256490">
    <ele>36.2</ele>
    <time>2024-09-12T12:09:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6380220" lon="-5.2255660">
    <ele>36.0</ele>
    <time>2024-09-12T12:09:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6380750" lon="-5.2254790">
    <ele>36.0</ele>
    <time>2024-09-12T12:09:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6381240" lon="-5.2253810">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6381720" lon="-5.2252740">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382040" lon="-5.2251580">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382310" lon="-5.2250360">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382470" lon="-5.2249100">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382630" lon="-5.2247810">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382630" lon="-5.2246540">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382630" lon="-5.2245260">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382630" lon="-5.2244020">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382630" lon="-5.2242750">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382580" lon="-5.2241510">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382520" lon="-5.2240270">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382470" lon="-5.2239060">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382470" lon="-5.2237840">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382470" lon="-5.2236620">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382630" lon="-5.2235460">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6382950" lon="-5.2234410">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383440" lon="-5.2233490">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6383970" lon="-5.2232800">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6384560" lon="-5.2232350">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385210" lon="-5.2232210">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6385850" lon="-5.2232180">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6386490" lon="-5.2232160">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6387140" lon="-5.2232140">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6387780" lon="-5.2232120">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6388430" lon="-5.2232110">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6389070" lon="-5.2232110">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6389710" lon="-5.2232120">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6390360" lon="-5.2232150">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6390950" lon="-5.2232210">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6391590" lon="-5.2232240">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6392290" lon="-5.2232240">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6392930" lon="-5.2232220">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6393520" lon="-5.2232190">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6394170" lon="-5.2232130">
    <ele>35.8</ele>
    <time>2024-09-12T12:09:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6394760" lon="-5.2232060">
    <ele>35.6</ele>
    <time>2024-09-12T12:09:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6395450" lon="-5.2231960">
    <ele>35.6</ele>
    <time>2024-09-12T12:09:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6396100" lon="-5.2231830">
    <ele>35.4</ele>
    <time>2024-09-12T12:09:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>105</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6396740" lon="-5.2231700">
    <ele>35.2</ele>
    <time>2024-09-12T12:09:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6397440" lon="-5.2231530">
    <ele>35.0</ele>
    <time>2024-09-12T12:09:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6398190" lon="-5.2231370">
    <ele>34.8</ele>
    <time>2024-09-12T12:09:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6398890" lon="-5.2231190">
    <ele>34.6</ele>
    <time>2024-09-12T12:09:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6399640" lon="-5.2231000">
    <ele>34.2</ele>
    <time>2024-09-12T12:09:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6400440" lon="-5.2230800">
    <ele>34.0</ele>
    <time>2024-09-12T12:09:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6401250" lon="-5.2230610">
    <ele>33.6</ele>
    <time>2024-09-12T12:09:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6402050" lon="-5.2230410">
    <ele>33.4</ele>
    <time>2024-09-12T12:09:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6402860" lon="-5.2230210">
    <ele>33.0</ele>
    <time>2024-09-12T12:09:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6403710" lon="-5.2230010">
    <ele>32.8</ele>
    <time>2024-09-12T12:09:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6404570" lon="-5.2229800">
    <ele>32.4</ele>
    <time>2024-09-12T12:09:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>112</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6405480" lon="-5.2229600">
    <ele>32.0</ele>
    <time>2024-09-12T12:09:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6406400" lon="-5.2229380">
    <ele>31.8</ele>
    <time>2024-09-12T12:09:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6407310" lon="-5.2229170">
    <ele>31.4</ele>
    <time>2024-09-12T12:09:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6408220" lon="-5.2228950">
    <ele>31.0</ele>
    <time>2024-09-12T12:09:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6409190" lon="-5.2228720">
    <ele>30.6</ele>
    <time>2024-09-12T12:09:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>112</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6410150" lon="-5.2228480">
    <ele>30.2</ele>
    <time>2024-09-12T12:10:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6411120" lon="-5.2228230">
    <ele>30.0</ele>
    <time>2024-09-12T12:10:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6412080" lon="-5.2227950">
    <ele>29.6</ele>
    <time>2024-09-12T12:10:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413100" lon="-5.2227660">
    <ele>29.4</ele>
    <time>2024-09-12T12:10:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6414070" lon="-5.2227350">
    <ele>29.0</ele>
    <time>2024-09-12T12:10:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6415030" lon="-5.2227020">
    <ele>28.8</ele>
    <time>2024-09-12T12:10:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6416000" lon="-5.2226670">
    <ele>28.6</ele>
    <time>2024-09-12T12:10:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6416960" lon="-5.2226290">
    <ele>28.4</ele>
    <time>2024-09-12T12:10:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>112</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6417930" lon="-5.2225870">
    <ele>28.2</ele>
    <time>2024-09-12T12:10:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6418900" lon="-5.2225410">
    <ele>28.0</ele>
    <time>2024-09-12T12:10:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6419860" lon="-5.2224910">
    <ele>28.0</ele>
    <time>2024-09-12T12:10:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>114</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6420770" lon="-5.2224350">
    <ele>28.0</ele>
    <time>2024-09-12T12:10:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>112</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6421630" lon="-5.2223740">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>112</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6422540" lon="-5.2223160">
    <ele>27.6</ele>
    <time>2024-09-12T12:10:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6423460" lon="-5.2222680">
    <ele>27.6</ele>
    <time>2024-09-12T12:10:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6424370" lon="-5.2222440">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6425280" lon="-5.2222530">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6426190" lon="-5.2222680">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6427000" lon="-5.2222830">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6427910" lon="-5.2222970">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6428710" lon="-5.2223080">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6429570" lon="-5.2223100">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6430380" lon="-5.2222850">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6431070" lon="-5.2222120">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6431610" lon="-5.2221070">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6432150" lon="-5.2219950">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6432740" lon="-5.2219120">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6433490" lon="-5.2218710">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6434240" lon="-5.2218720">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6435040" lon="-5.2218990">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6435690" lon="-5.2219570">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6436220" lon="-5.2220490">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6436540" lon="-5.2221650">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6436870" lon="-5.2222870">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437240" lon="-5.2223940">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437720" lon="-5.2224840">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6438370" lon="-5.2225520">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6439010" lon="-5.2226020">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6439660" lon="-5.2226390">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6440350" lon="-5.2226660">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6441000" lon="-5.2226820">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6441690" lon="-5.2227030">
    <ele>27.6</ele>
    <time>2024-09-12T12:10:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6442340" lon="-5.2227470">
    <ele>27.6</ele>
    <time>2024-09-12T12:10:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6442930" lon="-5.2228150">
    <ele>27.6</ele>
    <time>2024-09-12T12:10:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6443410" lon="-5.2228960">
    <ele>27.8</ele>
    <time>2024-09-12T12:10:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6443890" lon="-5.2229850">
    <ele>28.0</ele>
    <time>2024-09-12T12:10:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444160" lon="-5.2230850">
    <ele>28.2</ele>
    <time>2024-09-12T12:10:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444320" lon="-5.2231880">
    <ele>28.4</ele>
    <time>2024-09-12T12:10:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>95</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444480" lon="-5.2232850">
    <ele>28.8</ele>
    <time>2024-09-12T12:10:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>92</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444640" lon="-5.2233800">
    <ele>29.0</ele>
    <time>2024-09-12T12:10:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>92</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444810" lon="-5.2234710">
    <ele>29.2</ele>
    <time>2024-09-12T12:10:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>92</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444970" lon="-5.2235570">
    <ele>29.4</ele>
    <time>2024-09-12T12:10:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>90</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6445180" lon="-5.2236340">
    <ele>29.6</ele>
    <time>2024-09-12T12:10:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6445450" lon="-5.2236990">
    <ele>29.8</ele>
    <time>2024-09-12T12:10:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6445770" lon="-5.2237500">
    <ele>30.0</ele>
    <time>2024-09-12T12:10:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6446150" lon="-5.2237890">
    <ele>30.0</ele>
    <time>2024-09-12T12:10:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6446520" lon="-5.2238180">
    <ele>30.2</ele>
    <time>2024-09-12T12:10:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6446950" lon="-5.2238340">
    <ele>30.4</ele>
    <time>2024-09-12T12:10:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6447270" lon="-5.2238380">
    <ele>30.6</ele>
    <time>2024-09-12T12:10:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6447600" lon="-5.2238330">
    <ele>30.8</ele>
    <time>2024-09-12T12:10:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6447920" lon="-5.2238190">
    <ele>31.0</ele>
    <time>2024-09-12T12:11:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6448240" lon="-5.2238000">
    <ele>31.2</ele>
    <time>2024-09-12T12:11:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6448510" lon="-5.2237770">
    <ele>31.4</ele>
    <time>2024-09-12T12:11:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6448720" lon="-5.2237510">
    <ele>31.4</ele>
    <time>2024-09-12T12:11:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>82</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6448940" lon="-5.2237230">
    <ele>31.6</ele>
    <time>2024-09-12T12:11:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449150" lon="-5.2236950">
    <ele>31.6</ele>
    <time>2024-09-12T12:11:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449310" lon="-5.2236640">
    <ele>31.8</ele>
    <time>2024-09-12T12:11:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>82</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449470" lon="-5.2236340">
    <ele>32.0</ele>
    <time>2024-09-12T12:11:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>82</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449630" lon="-5.2236010">
    <ele>32.0</ele>
    <time>2024-09-12T12:11:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449850" lon="-5.2235690">
    <ele>32.2</ele>
    <time>2024-09-12T12:11:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449960" lon="-5.2235360">
    <ele>32.2</ele>
    <time>2024-09-12T12:11:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450120" lon="-5.2235040">
    <ele>32.2</ele>
    <time>2024-09-12T12:11:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450280" lon="-5.2234700">
    <ele>32.4</ele>
    <time>2024-09-12T12:11:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450440" lon="-5.2234370">
    <ele>32.4</ele>
    <time>2024-09-12T12:11:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450600" lon="-5.2234040">
    <ele>32.4</ele>
    <time>2024-09-12T12:11:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450760" lon="-5.2233690">
    <ele>32.6</ele>
    <time>2024-09-12T12:11:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450920" lon="-5.2233350">
    <ele>32.6</ele>
    <time>2024-09-12T12:11:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451080" lon="-5.2232990">
    <ele>32.6</ele>
    <time>2024-09-12T12:11:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>53</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451240" lon="-5.2232620">
    <ele>32.6</ele>
    <time>2024-09-12T12:11:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>53</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451400" lon="-5.2232250">
    <ele>32.8</ele>
    <time>2024-09-12T12:11:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451570" lon="-5.2231870">
    <ele>32.8</ele>
    <time>2024-09-12T12:11:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451730" lon="-5.2231480">
    <ele>32.8</ele>
    <time>2024-09-12T12:11:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451890" lon="-5.2231090">
    <ele>32.8</ele>
    <time>2024-09-12T12:11:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452100" lon="-5.2230720">
    <ele>32.8</ele>
    <time>2024-09-12T12:11:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452260" lon="-5.2230320">
    <ele>33.0</ele>
    <time>2024-09-12T12:11:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452480" lon="-5.2229940">
    <ele>33.0</ele>
    <time>2024-09-12T12:11:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452690" lon="-5.2229540">
    <ele>33.0</ele>
    <time>2024-09-12T12:11:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452910" lon="-5.2229180">
    <ele>33.0</ele>
    <time>2024-09-12T12:11:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6453170" lon="-5.2228830">
    <ele>33.0</ele>
    <time>2024-09-12T12:11:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>48</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6453440" lon="-5.2228510">
    <ele>33.0</ele>
    <time>2024-09-12T12:11:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6453820" lon="-5.2228210">
    <ele>33.0</ele>
    <time>2024-09-12T12:11:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6454140" lon="-5.2227970">
    <ele>32.8</ele>
    <time>2024-09-12T12:11:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6454520" lon="-5.2227760">
    <ele>32.8</ele>
    <time>2024-09-12T12:11:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6454890" lon="-5.2227600">
    <ele>32.8</ele>
    <time>2024-09-12T12:11:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6455370" lon="-5.2227510">
    <ele>32.6</ele>
    <time>2024-09-12T12:11:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6455800" lon="-5.2227480">
    <ele>32.4</ele>
    <time>2024-09-12T12:11:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6456290" lon="-5.2227510">
    <ele>32.4</ele>
    <time>2024-09-12T12:11:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6456820" lon="-5.2227610">
    <ele>32.2</ele>
    <time>2024-09-12T12:11:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6457360" lon="-5.2227780">
    <ele>32.0</ele>
    <time>2024-09-12T12:11:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6457950" lon="-5.2228020">
    <ele>31.8</ele>
    <time>2024-09-12T12:11:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6458540" lon="-5.2228330">
    <ele>31.6</ele>
    <time>2024-09-12T12:11:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6459130" lon="-5.2228710">
    <ele>31.4</ele>
    <time>2024-09-12T12:11:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6459720" lon="-5.2229190">
    <ele>31.2</ele>
    <time>2024-09-12T12:11:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6460360" lon="-5.2229770">
    <ele>31.0</ele>
    <time>2024-09-12T12:11:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6460950" lon="-5.2230480">
    <ele>30.8</ele>
    <time>2024-09-12T12:11:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>112</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6461490" lon="-5.2231260">
    <ele>30.6</ele>
    <time>2024-09-12T12:11:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6462030" lon="-5.2232190">
    <ele>30.6</ele>
    <time>2024-09-12T12:11:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6462510" lon="-5.2233180">
    <ele>30.4</ele>
    <time>2024-09-12T12:11:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6462940" lon="-5.2234300">
    <ele>30.4</ele>
    <time>2024-09-12T12:11:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6463310" lon="-5.2235460">
    <ele>30.2</ele>
    <time>2024-09-12T12:11:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6463580" lon="-5.2236690">
    <ele>30.2</ele>
    <time>2024-09-12T12:11:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>105</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6463850" lon="-5.2237990">
    <ele>30.0</ele>
    <time>2024-09-12T12:11:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6463960" lon="-5.2239300">
    <ele>30.0</ele>
    <time>2024-09-12T12:11:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464120" lon="-5.2240600">
    <ele>30.0</ele>
    <time>2024-09-12T12:11:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464230" lon="-5.2241930">
    <ele>30.0</ele>
    <time>2024-09-12T12:11:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464280" lon="-5.2243250">
    <ele>29.8</ele>
    <time>2024-09-12T12:11:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464440" lon="-5.2244580">
    <ele>29.8</ele>
    <time>2024-09-12T12:11:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>105</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464600" lon="-5.2245900">
    <ele>29.8</ele>
    <time>2024-09-12T12:11:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464760" lon="-5.2247190">
    <ele>29.6</ele>
    <time>2024-09-12T12:11:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6465030" lon="-5.2248480">
    <ele>29.6</ele>
    <time>2024-09-12T12:11:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6465300" lon="-5.2249730">
    <ele>29.4</ele>
    <time>2024-09-12T12:12:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>105</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6465620" lon="-5.2250990">
    <ele>29.2</ele>
    <time>2024-09-12T12:12:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6466000" lon="-5.2252200">
    <ele>29.2</ele>
    <time>2024-09-12T12:12:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6466420" lon="-5.2253380">
    <ele>29.0</ele>
    <time>2024-09-12T12:12:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6466850" lon="-5.2254490">
    <ele>28.8</ele>
    <time>2024-09-12T12:12:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>113</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6467390" lon="-5.2255560">
    <ele>28.6</ele>
    <time>2024-09-12T12:12:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6467980" lon="-5.2256600">
    <ele>28.4</ele>
    <time>2024-09-12T12:12:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6468570" lon="-5.2257500">
    <ele>28.4</ele>
    <time>2024-09-12T12:12:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6469320" lon="-5.2258310">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6470020" lon="-5.2258970">
    <ele>28.0</ele>
    <time>2024-09-12T12:12:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6470820" lon="-5.2259480">
    <ele>27.8</ele>
    <time>2024-09-12T12:12:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6471630" lon="-5.2259790">
    <ele>27.6</ele>
    <time>2024-09-12T12:12:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6472490" lon="-5.2259980">
    <ele>27.6</ele>
    <time>2024-09-12T12:12:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6473340" lon="-5.2260210">
    <ele>27.4</ele>
    <time>2024-09-12T12:12:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>113</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6474150" lon="-5.2260550">
    <ele>27.2</ele>
    <time>2024-09-12T12:12:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>113</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6474950" lon="-5.2261010">
    <ele>27.0</ele>
    <time>2024-09-12T12:12:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6475760" lon="-5.2261600">
    <ele>27.0</ele>
    <time>2024-09-12T12:12:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6476510" lon="-5.2262320">
    <ele>26.8</ele>
    <time>2024-09-12T12:12:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6477260" lon="-5.2263140">
    <ele>26.6</ele>
    <time>2024-09-12T12:12:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6477960" lon="-5.2264050">
    <ele>26.4</ele>
    <time>2024-09-12T12:12:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6478600" lon="-5.2265070">
    <ele>26.4</ele>
    <time>2024-09-12T12:12:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479140" lon="-5.2266180">
    <ele>26.4</ele>
    <time>2024-09-12T12:12:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479670" lon="-5.2267330">
    <ele>26.4</ele>
    <time>2024-09-12T12:12:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480210" lon="-5.2268520">
    <ele>26.6</ele>
    <time>2024-09-12T12:12:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480640" lon="-5.2269760">
    <ele>26.6</ele>
    <time>2024-09-12T12:12:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481070" lon="-5.2270930">
    <ele>26.8</ele>
    <time>2024-09-12T12:12:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481500" lon="-5.2272100">
    <ele>26.8</ele>
    <time>2024-09-12T12:12:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481870" lon="-5.2273210">
    <ele>27.0</ele>
    <time>2024-09-12T12:12:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482250" lon="-5.2274330">
    <ele>27.0</ele>
    <time>2024-09-12T12:12:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482570" lon="-5.2275430">
    <ele>27.2</ele>
    <time>2024-09-12T12:12:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482950" lon="-5.2276490">
    <ele>27.2</ele>
    <time>2024-09-12T12:12:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483270" lon="-5.2277560">
    <ele>27.4</ele>
    <time>2024-09-12T12:12:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483590" lon="-5.2278590">
    <ele>27.4</ele>
    <time>2024-09-12T12:12:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483910" lon="-5.2279610">
    <ele>27.6</ele>
    <time>2024-09-12T12:12:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484180" lon="-5.2280600">
    <ele>27.6</ele>
    <time>2024-09-12T12:12:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484450" lon="-5.2281580">
    <ele>27.8</ele>
    <time>2024-09-12T12:12:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484770" lon="-5.2282540">
    <ele>27.8</ele>
    <time>2024-09-12T12:12:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485040" lon="-5.2283470">
    <ele>28.0</ele>
    <time>2024-09-12T12:12:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485250" lon="-5.2284370">
    <ele>28.0</ele>
    <time>2024-09-12T12:12:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485520" lon="-5.2285210">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485900" lon="-5.2286030">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6486220" lon="-5.2286780">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6486540" lon="-5.2287470">
    <ele>28.4</ele>
    <time>2024-09-12T12:12:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6486970" lon="-5.2288110">
    <ele>28.4</ele>
    <time>2024-09-12T12:12:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6487400" lon="-5.2288670">
    <ele>28.4</ele>
    <time>2024-09-12T12:12:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6487880" lon="-5.2289140">
    <ele>28.4</ele>
    <time>2024-09-12T12:12:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6488360" lon="-5.2289560">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6488900" lon="-5.2289830">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6489440" lon="-5.2289970">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6489970" lon="-5.2289980">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6490510" lon="-5.2289850">
    <ele>28.2</ele>
    <time>2024-09-12T12:12:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6491100" lon="-5.2289570">
    <ele>28.0</ele>
    <time>2024-09-12T12:12:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6491640" lon="-5.2289150">
    <ele>28.0</ele>
    <time>2024-09-12T12:12:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6492120" lon="-5.2288610">
    <ele>28.0</ele>
    <time>2024-09-12T12:12:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6492600" lon="-5.2287960">
    <ele>27.8</ele>
    <time>2024-09-12T12:12:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6493090" lon="-5.2287210">
    <ele>27.8</ele>
    <time>2024-09-12T12:12:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6493510" lon="-5.2286390">
    <ele>27.8</ele>
    <time>2024-09-12T12:12:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6493940" lon="-5.2285510">
    <ele>27.6</ele>
    <time>2024-09-12T12:12:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6494320" lon="-5.2284620">
    <ele>27.6</ele>
    <time>2024-09-12T12:12:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6494690" lon="-5.2283700">
    <ele>27.4</ele>
    <time>2024-09-12T12:12:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6495120" lon="-5.2282760">
    <ele>27.2</ele>
    <time>2024-09-12T12:13:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6495550" lon="-5.2281790">
    <ele>27.2</ele>
    <time>2024-09-12T12:13:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6495930" lon="-5.2280840">
    <ele>27.0</ele>
    <time>2024-09-12T12:13:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6496360" lon="-5.2279870">
    <ele>27.0</ele>
    <time>2024-09-12T12:13:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6496790" lon="-5.2278910">
    <ele>26.8</ele>
    <time>2024-09-12T12:13:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6497270" lon="-5.2277940">
    <ele>26.8</ele>
    <time>2024-09-12T12:13:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6497750" lon="-5.2277040">
    <ele>26.6</ele>
    <time>2024-09-12T12:13:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6498400" lon="-5.2276340">
    <ele>26.6</ele>
    <time>2024-09-12T12:13:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6499040" lon="-5.2275890">
    <ele>26.6</ele>
    <time>2024-09-12T12:13:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6499740" lon="-5.2275680">
    <ele>26.6</ele>
    <time>2024-09-12T12:13:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6500490" lon="-5.2275680">
    <ele>26.4</ele>
    <time>2024-09-12T12:13:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6501190" lon="-5.2275860">
    <ele>26.4</ele>
    <time>2024-09-12T12:13:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6501880" lon="-5.2276180">
    <ele>26.2</ele>
    <time>2024-09-12T12:13:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6502630" lon="-5.2276600">
    <ele>26.0</ele>
    <time>2024-09-12T12:13:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6503330" lon="-5.2277090">
    <ele>25.6</ele>
    <time>2024-09-12T12:13:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504080" lon="-5.2277610">
    <ele>25.4</ele>
    <time>2024-09-12T12:13:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504780" lon="-5.2278210">
    <ele>25.2</ele>
    <time>2024-09-12T12:13:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505530" lon="-5.2278840">
    <ele>25.0</ele>
    <time>2024-09-12T12:13:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506280" lon="-5.2279520">
    <ele>24.6</ele>
    <time>2024-09-12T12:13:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6507030" lon="-5.2280200">
    <ele>24.4</ele>
    <time>2024-09-12T12:13:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6507780" lon="-5.2280930">
    <ele>24.2</ele>
    <time>2024-09-12T12:13:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6508590" lon="-5.2281650">
    <ele>23.8</ele>
    <time>2024-09-12T12:13:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509340" lon="-5.2282380">
    <ele>23.6</ele>
    <time>2024-09-12T12:13:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6510140" lon="-5.2283120">
    <ele>23.2</ele>
    <time>2024-09-12T12:13:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511000" lon="-5.2283830">
    <ele>23.0</ele>
    <time>2024-09-12T12:13:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>105</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511810" lon="-5.2284490">
    <ele>22.6</ele>
    <time>2024-09-12T12:13:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6512670" lon="-5.2285100">
    <ele>22.4</ele>
    <time>2024-09-12T12:13:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6513520" lon="-5.2285640">
    <ele>22.4</ele>
    <time>2024-09-12T12:13:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6514440" lon="-5.2286110">
    <ele>22.4</ele>
    <time>2024-09-12T12:13:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6515290" lon="-5.2286520">
    <ele>22.2</ele>
    <time>2024-09-12T12:13:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6516150" lon="-5.2286820">
    <ele>22.2</ele>
    <time>2024-09-12T12:13:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517060" lon="-5.2286990">
    <ele>22.2</ele>
    <time>2024-09-12T12:13:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517920" lon="-5.2286870">
    <ele>22.2</ele>
    <time>2024-09-12T12:13:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6518730" lon="-5.2286280">
    <ele>22.2</ele>
    <time>2024-09-12T12:13:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519420" lon="-5.2285380">
    <ele>22.2</ele>
    <time>2024-09-12T12:13:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519960" lon="-5.2284290">
    <ele>22.0</ele>
    <time>2024-09-12T12:13:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520500" lon="-5.2283120">
    <ele>22.0</ele>
    <time>2024-09-12T12:13:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6521030" lon="-5.2281990">
    <ele>22.0</ele>
    <time>2024-09-12T12:13:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6521680" lon="-5.2281180">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6522480" lon="-5.2280880">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6523340" lon="-5.2281110">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6524040" lon="-5.2281610">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6524790" lon="-5.2282240">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6525490" lon="-5.2282880">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6526180" lon="-5.2283510">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6526880" lon="-5.2284080">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6527630" lon="-5.2284580">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6528330" lon="-5.2284880">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529080" lon="-5.2284980">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529830" lon="-5.2284850">
    <ele>21.8</ele>
    <time>2024-09-12T12:13:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530530" lon="-5.2284490">
    <ele>22.0</ele>
    <time>2024-09-12T12:13:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531170" lon="-5.2283940">
    <ele>22.0</ele>
    <time>2024-09-12T12:13:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531760" lon="-5.2283270">
    <ele>22.0</ele>
    <time>2024-09-12T12:13:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6532350" lon="-5.2282520">
    <ele>22.2</ele>
    <time>2024-09-12T12:13:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6532840" lon="-5.2281730">
    <ele>22.2</ele>
    <time>2024-09-12T12:13:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6533320" lon="-5.2280930">
    <ele>22.4</ele>
    <time>2024-09-12T12:13:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6533800" lon="-5.2280140">
    <ele>22.4</ele>
    <time>2024-09-12T12:13:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6534280" lon="-5.2279390">
    <ele>22.6</ele>
    <time>2024-09-12T12:13:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6534770" lon="-5.2278690">
    <ele>22.6</ele>
    <time>2024-09-12T12:13:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535250" lon="-5.2278090">
    <ele>22.8</ele>
    <time>2024-09-12T12:13:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535790" lon="-5.2277620">
    <ele>23.0</ele>
    <time>2024-09-12T12:14:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6536320" lon="-5.2277380">
    <ele>23.2</ele>
    <time>2024-09-12T12:14:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6536860" lon="-5.2277290">
    <ele>23.4</ele>
    <time>2024-09-12T12:14:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6537400" lon="-5.2277400">
    <ele>23.6</ele>
    <time>2024-09-12T12:14:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6537880" lon="-5.2277560">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>93</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6538310" lon="-5.2277810">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>89</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6538740" lon="-5.2278120">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6539220" lon="-5.2278510">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6539650" lon="-5.2278950">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6540080" lon="-5.2279480">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6540450" lon="-5.2279950">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6540830" lon="-5.2280480">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6541260" lon="-5.2281030">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6541690" lon="-5.2281590">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6542060" lon="-5.2282150">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6542490" lon="-5.2282710">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6542920" lon="-5.2283260">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6543350" lon="-5.2283820">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6543730" lon="-5.2284370">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6544100" lon="-5.2284940">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6544530" lon="-5.2285500">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6544960" lon="-5.2286080">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6545390" lon="-5.2286650">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6545760" lon="-5.2287220">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6546190" lon="-5.2287800">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6546620" lon="-5.2288380">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6547050" lon="-5.2288950">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6547430" lon="-5.2289520">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6547860" lon="-5.2290100">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6548230" lon="-5.2290690">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6548660" lon="-5.2291290">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6549090" lon="-5.2291880">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6549520" lon="-5.2292450">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6549950" lon="-5.2292980">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6550430" lon="-5.2293470">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6550910" lon="-5.2293920">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6551400" lon="-5.2294330">
    <ele>23.6</ele>
    <time>2024-09-12T12:14:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6551930" lon="-5.2294670">
    <ele>23.2</ele>
    <time>2024-09-12T12:14:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6552580" lon="-5.2294880">
    <ele>23.0</ele>
    <time>2024-09-12T12:14:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6553220" lon="-5.2294910">
    <ele>22.8</ele>
    <time>2024-09-12T12:14:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6553860" lon="-5.2294700">
    <ele>22.8</ele>
    <time>2024-09-12T12:14:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6554510" lon="-5.2294290">
    <ele>23.0</ele>
    <time>2024-09-12T12:14:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6555040" lon="-5.2293750">
    <ele>23.2</ele>
    <time>2024-09-12T12:14:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6555470" lon="-5.2293080">
    <ele>23.2</ele>
    <time>2024-09-12T12:14:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6555850" lon="-5.2292330">
    <ele>23.4</ele>
    <time>2024-09-12T12:14:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6556220" lon="-5.2291530">
    <ele>23.6</ele>
    <time>2024-09-12T12:14:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6556550" lon="-5.2290730">
    <ele>23.6</ele>
    <time>2024-09-12T12:14:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6556920" lon="-5.2289950">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6557190" lon="-5.2289230">
    <ele>23.8</ele>
    <time>2024-09-12T12:14:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6557570" lon="-5.2288520">
    <ele>24.0</ele>
    <time>2024-09-12T12:14:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6557890" lon="-5.2287840">
    <ele>24.0</ele>
    <time>2024-09-12T12:14:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6558210" lon="-5.2287180">
    <ele>24.2</ele>
    <time>2024-09-12T12:14:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6558530" lon="-5.2286560">
    <ele>24.4</ele>
    <time>2024-09-12T12:14:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6558800" lon="-5.2285940">
    <ele>24.4</ele>
    <time>2024-09-12T12:14:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6559120" lon="-5.2285330">
    <ele>24.6</ele>
    <time>2024-09-12T12:14:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6559390" lon="-5.2284730">
    <ele>24.6</ele>
    <time>2024-09-12T12:14:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6559600" lon="-5.2284120">
    <ele>24.8</ele>
    <time>2024-09-12T12:14:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6559820" lon="-5.2283510">
    <ele>24.8</ele>
    <time>2024-09-12T12:14:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560090" lon="-5.2282880">
    <ele>24.8</ele>
    <time>2024-09-12T12:14:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560250" lon="-5.2282240">
    <ele>25.0</ele>
    <time>2024-09-12T12:14:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560410" lon="-5.2281600">
    <ele>25.0</ele>
    <time>2024-09-12T12:15:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560570" lon="-5.2280940">
    <ele>25.2</ele>
    <time>2024-09-12T12:15:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560680" lon="-5.2280260">
    <ele>25.2</ele>
    <time>2024-09-12T12:15:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560780" lon="-5.2279580">
    <ele>25.2</ele>
    <time>2024-09-12T12:15:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560890" lon="-5.2278900">
    <ele>25.2</ele>
    <time>2024-09-12T12:15:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560950" lon="-5.2278200">
    <ele>25.4</ele>
    <time>2024-09-12T12:15:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6561000" lon="-5.2277500">
    <ele>25.4</ele>
    <time>2024-09-12T12:15:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6561160" lon="-5.2276820">
    <ele>25.4</ele>
    <time>2024-09-12T12:15:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6561270" lon="-5.2276120">
    <ele>25.4</ele>
    <time>2024-09-12T12:15:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6561370" lon="-5.2275410">
    <ele>25.4</ele>
    <time>2024-09-12T12:15:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6561540" lon="-5.2274740">
    <ele>25.4</ele>
    <time>2024-09-12T12:15:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6561750" lon="-5.2274090">
    <ele>25.6</ele>
    <time>2024-09-12T12:15:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6561960" lon="-5.2273500">
    <ele>25.6</ele>
    <time>2024-09-12T12:15:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6562230" lon="-5.2272970">
    <ele>25.8</ele>
    <time>2024-09-12T12:15:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6562500" lon="-5.2272510">
    <ele>25.8</ele>
    <time>2024-09-12T12:15:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6562820" lon="-5.2272100">
    <ele>26.0</ele>
    <time>2024-09-12T12:15:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>123</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6563140" lon="-5.2271750">
    <ele>26.2</ele>
    <time>2024-09-12T12:15:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>94</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6563410" lon="-5.2271440">
    <ele>26.2</ele>
    <time>2024-09-12T12:15:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>94</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6563790" lon="-5.2271170">
    <ele>26.4</ele>
    <time>2024-09-12T12:15:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>97</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6564110" lon="-5.2270930">
    <ele>26.4</ele>
    <time>2024-09-12T12:15:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>94</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6564430" lon="-5.2270720">
    <ele>26.4</ele>
    <time>2024-09-12T12:15:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>94</gpxtpx:watts>
      <gpxtpx:cad>66</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6564860" lon="-5.2270550">
    <ele>26.6</ele>
    <time>2024-09-12T12:15:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>102</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6565240" lon="-5.2270420">
    <ele>26.6</ele>
    <time>2024-09-12T12:15:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>118</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6565610" lon="-5.2270340">
    <ele>26.8</ele>
    <time>2024-09-12T12:15:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>130</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6565990" lon="-5.2270310">
    <ele>26.8</ele>
    <time>2024-09-12T12:15:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>144</gpxtpx:watts>
      <gpxtpx:cad>68</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566420" lon="-5.2270370">
    <ele>27.0</ele>
    <time>2024-09-12T12:15:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>141</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566850" lon="-5.2270520">
    <ele>27.0</ele>
    <time>2024-09-12T12:15:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>137</gpxtpx:watts>
      <gpxtpx:cad>66</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567220" lon="-5.2270790">
    <ele>27.2</ele>
    <time>2024-09-12T12:15:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>123</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567600" lon="-5.2271180">
    <ele>27.4</ele>
    <time>2024-09-12T12:15:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>148</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567870" lon="-5.2271650">
    <ele>27.4</ele>
    <time>2024-09-12T12:15:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>162</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568240" lon="-5.2272210">
    <ele>27.6</ele>
    <time>2024-09-12T12:15:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>184</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568510" lon="-5.2272770">
    <ele>27.8</ele>
    <time>2024-09-12T12:15:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>155</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568780" lon="-5.2273360">
    <ele>28.0</ele>
    <time>2024-09-12T12:15:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>144</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569050" lon="-5.2273960">
    <ele>28.2</ele>
    <time>2024-09-12T12:15:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>148</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569210" lon="-5.2274560">
    <ele>28.6</ele>
    <time>2024-09-12T12:15:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>137</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569420" lon="-5.2275150">
    <ele>28.8</ele>
    <time>2024-09-12T12:15:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>137</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569580" lon="-5.2275740">
    <ele>29.0</ele>
    <time>2024-09-12T12:15:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>163</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569740" lon="-5.2276330">
    <ele>29.2</ele>
    <time>2024-09-12T12:15:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>175</gpxtpx:watts>
      <gpxtpx:cad>66</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569850" lon="-5.2276930">
    <ele>29.6</ele>
    <time>2024-09-12T12:15:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>154</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569900" lon="-5.2277500">
    <ele>29.8</ele>
    <time>2024-09-12T12:15:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>161</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569900" lon="-5.2278070">
    <ele>30.0</ele>
    <time>2024-09-12T12:15:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>156</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569850" lon="-5.2278600">
    <ele>30.2</ele>
    <time>2024-09-12T12:15:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>163</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569740" lon="-5.2279070">
    <ele>30.6</ele>
    <time>2024-09-12T12:15:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>158</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569580" lon="-5.2279470">
    <ele>30.8</ele>
    <time>2024-09-12T12:15:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>150</gpxtpx:watts>
      <gpxtpx:cad>60</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569370" lon="-5.2279780">
    <ele>30.8</ele>
    <time>2024-09-12T12:15:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>140</gpxtpx:watts>
      <gpxtpx:cad>59</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569100" lon="-5.2280070">
    <ele>31.0</ele>
    <time>2024-09-12T12:15:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>152</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568830" lon="-5.2280360">
    <ele>31.0</ele>
    <time>2024-09-12T12:15:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>145</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568560" lon="-5.2280660">
    <ele>31.2</ele>
    <time>2024-09-12T12:15:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>112</gpxtpx:watts>
      <gpxtpx:cad>60</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568290" lon="-5.2280970">
    <ele>31.2</ele>
    <time>2024-09-12T12:15:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>115</gpxtpx:watts>
      <gpxtpx:cad>59</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568030" lon="-5.2281310">
    <ele>31.4</ele>
    <time>2024-09-12T12:15:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>109</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567760" lon="-5.2281680">
    <ele>31.6</ele>
    <time>2024-09-12T12:15:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>102</gpxtpx:watts>
      <gpxtpx:cad>59</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567490" lon="-5.2282070">
    <ele>31.6</ele>
    <time>2024-09-12T12:15:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567280" lon="-5.2282490">
    <ele>31.8</ele>
    <time>2024-09-12T12:15:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567060" lon="-5.2282900">
    <ele>31.8</ele>
    <time>2024-09-12T12:15:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566850" lon="-5.2283340">
    <ele>31.8</ele>
    <time>2024-09-12T12:15:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566690" lon="-5.2283800">
    <ele>32.0</ele>
    <time>2024-09-12T12:15:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>62</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566580" lon="-5.2284280">
    <ele>32.0</ele>
    <time>2024-09-12T12:15:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566420" lon="-5.2284770">
    <ele>32.2</ele>
    <time>2024-09-12T12:15:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566310" lon="-5.2285270">
    <ele>32.2</ele>
    <time>2024-09-12T12:15:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566200" lon="-5.2285800">
    <ele>32.2</ele>
    <time>2024-09-12T12:15:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566150" lon="-5.2286330">
    <ele>32.4</ele>
    <time>2024-09-12T12:16:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566150" lon="-5.2286890">
    <ele>32.4</ele>
    <time>2024-09-12T12:16:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>60</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566150" lon="-5.2287460">
    <ele>32.4</ele>
    <time>2024-09-12T12:16:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>60</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566150" lon="-5.2288030">
    <ele>32.4</ele>
    <time>2024-09-12T12:16:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>58</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566150" lon="-5.2288600">
    <ele>32.4</ele>
    <time>2024-09-12T12:16:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>43</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566260" lon="-5.2289170">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>66</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566310" lon="-5.2289730">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566420" lon="-5.2290300">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>49</gpxtpx:watts>
      <gpxtpx:cad>66</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566520" lon="-5.2290870">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566690" lon="-5.2291420">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>68</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566850" lon="-5.2291980">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>44</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566950" lon="-5.2292520">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>44</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567170" lon="-5.2293040">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567380" lon="-5.2293540">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567650" lon="-5.2294040">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>45</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567920" lon="-5.2294500">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>48</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568240" lon="-5.2294930">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568560" lon="-5.2295310">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568940" lon="-5.2295570">
    <ele>32.6</ele>
    <time>2024-09-12T12:16:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569310" lon="-5.2295780">
    <ele>32.8</ele>
    <time>2024-09-12T12:16:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569690" lon="-5.2295950">
    <ele>32.8</ele>
    <time>2024-09-12T12:16:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6570010" lon="-5.2296100">
    <ele>33.0</ele>
    <time>2024-09-12T12:16:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>68</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6570390" lon="-5.2296220">
    <ele>33.2</ele>
    <time>2024-09-12T12:16:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6570710" lon="-5.2296320">
    <ele>33.2</ele>
    <time>2024-09-12T12:16:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6571030" lon="-5.2296410">
    <ele>33.4</ele>
    <time>2024-09-12T12:16:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6571300" lon="-5.2296480">
    <ele>33.4</ele>
    <time>2024-09-12T12:16:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6571620" lon="-5.2296540">
    <ele>33.6</ele>
    <time>2024-09-12T12:16:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6571890" lon="-5.2296590">
    <ele>33.8</ele>
    <time>2024-09-12T12:16:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6572160" lon="-5.2296640">
    <ele>33.8</ele>
    <time>2024-09-12T12:16:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6572430" lon="-5.2296680">
    <ele>34.0</ele>
    <time>2024-09-12T12:16:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6572640" lon="-5.2296720">
    <ele>34.0</ele>
    <time>2024-09-12T12:16:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6572910" lon="-5.2296750">
    <ele>34.2</ele>
    <time>2024-09-12T12:16:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6573180" lon="-5.2296780">
    <ele>34.2</ele>
    <time>2024-09-12T12:16:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6573390" lon="-5.2296810">
    <ele>34.4</ele>
    <time>2024-09-12T12:16:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6573610" lon="-5.2296840">
    <ele>34.4</ele>
    <time>2024-09-12T12:16:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6573820" lon="-5.2296860">
    <ele>34.6</ele>
    <time>2024-09-12T12:16:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6574090" lon="-5.2296890">
    <ele>34.6</ele>
    <time>2024-09-12T12:16:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6574300" lon="-5.2296920">
    <ele>34.8</ele>
    <time>2024-09-12T12:16:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6574520" lon="-5.2296940">
    <ele>34.8</ele>
    <time>2024-09-12T12:16:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6574730" lon="-5.2296970">
    <ele>35.0</ele>
    <time>2024-09-12T12:16:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6574950" lon="-5.2297000">
    <ele>35.0</ele>
    <time>2024-09-12T12:16:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6575160" lon="-5.2297030">
    <ele>35.2</ele>
    <time>2024-09-12T12:16:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6575430" lon="-5.2297060">
    <ele>35.2</ele>
    <time>2024-09-12T12:16:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>90</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6575640" lon="-5.2297090">
    <ele>35.4</ele>
    <time>2024-09-12T12:16:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>90</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6575860" lon="-5.2297130">
    <ele>35.4</ele>
    <time>2024-09-12T12:16:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6576070" lon="-5.2297170">
    <ele>35.6</ele>
    <time>2024-09-12T12:16:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6576340" lon="-5.2297220">
    <ele>35.6</ele>
    <time>2024-09-12T12:16:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6576610" lon="-5.2297280">
    <ele>35.8</ele>
    <time>2024-09-12T12:16:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6576820" lon="-5.2297340">
    <ele>35.8</ele>
    <time>2024-09-12T12:16:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6577040" lon="-5.2297410">
    <ele>35.8</ele>
    <time>2024-09-12T12:16:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>82</gpxtpx:watts>
      <gpxtpx:cad>69</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6577250" lon="-5.2297480">
    <ele>36.0</ele>
    <time>2024-09-12T12:16:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>69</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6577520" lon="-5.2297550">
    <ele>36.2</ele>
    <time>2024-09-12T12:16:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6577790" lon="-5.2297620">
    <ele>36.2</ele>
    <time>2024-09-12T12:16:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6578000" lon="-5.2297700">
    <ele>36.4</ele>
    <time>2024-09-12T12:16:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6578220" lon="-5.2297780">
    <ele>36.4</ele>
    <time>2024-09-12T12:16:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6578430" lon="-5.2297870">
    <ele>36.6</ele>
    <time>2024-09-12T12:16:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6578700" lon="-5.2297960">
    <ele>36.6</ele>
    <time>2024-09-12T12:16:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6578860" lon="-5.2298050">
    <ele>36.8</ele>
    <time>2024-09-12T12:16:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6579130" lon="-5.2298160">
    <ele>36.8</ele>
    <time>2024-09-12T12:16:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6579350" lon="-5.2298270">
    <ele>37.0</ele>
    <time>2024-09-12T12:16:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6579560" lon="-5.2298400">
    <ele>37.0</ele>
    <time>2024-09-12T12:17:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>88</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6579770" lon="-5.2298530">
    <ele>37.0</ele>
    <time>2024-09-12T12:17:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>90</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6580040" lon="-5.2298690">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6580310" lon="-5.2298850">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6580580" lon="-5.2299040">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6580790" lon="-5.2299240">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6581060" lon="-5.2299470">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>86</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6581380" lon="-5.2299730">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>82</gpxtpx:watts>
      <gpxtpx:cad>69</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6581600" lon="-5.2300010">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6581920" lon="-5.2300340">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>69</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6582190" lon="-5.2300670">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6582460" lon="-5.2301020">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6582670" lon="-5.2301380">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6582940" lon="-5.2301770">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6583260" lon="-5.2302150">
    <ele>37.8</ele>
    <time>2024-09-12T12:17:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6583530" lon="-5.2302520">
    <ele>37.8</ele>
    <time>2024-09-12T12:17:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6583850" lon="-5.2302870">
    <ele>37.8</ele>
    <time>2024-09-12T12:17:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6584170" lon="-5.2303220">
    <ele>37.8</ele>
    <time>2024-09-12T12:17:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6584550" lon="-5.2303550">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6584920" lon="-5.2303880">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6585300" lon="-5.2304210">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6585680" lon="-5.2304530">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6586100" lon="-5.2304850">
    <ele>37.6</ele>
    <time>2024-09-12T12:17:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6586530" lon="-5.2305180">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6586910" lon="-5.2305520">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6587390" lon="-5.2305870">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6587820" lon="-5.2306270">
    <ele>37.4</ele>
    <time>2024-09-12T12:17:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6588250" lon="-5.2306710">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6588730" lon="-5.2307210">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6589110" lon="-5.2307820">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6589430" lon="-5.2308530">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6589700" lon="-5.2309300">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6589970" lon="-5.2310140">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6590070" lon="-5.2311050">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6590180" lon="-5.2311960">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6590180" lon="-5.2312890">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6590130" lon="-5.2313820">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6589970" lon="-5.2314740">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6589750" lon="-5.2315630">
    <ele>37.2</ele>
    <time>2024-09-12T12:17:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6589430" lon="-5.2316450">
    <ele>37.0</ele>
    <time>2024-09-12T12:17:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6589110" lon="-5.2317230">
    <ele>37.0</ele>
    <time>2024-09-12T12:17:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6588680" lon="-5.2317930">
    <ele>37.0</ele>
    <time>2024-09-12T12:17:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6588250" lon="-5.2318570">
    <ele>37.0</ele>
    <time>2024-09-12T12:17:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6587710" lon="-5.2319100">
    <ele>37.0</ele>
    <time>2024-09-12T12:17:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6587180" lon="-5.2319550">
    <ele>36.8</ele>
    <time>2024-09-12T12:17:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6586640" lon="-5.2319870">
    <ele>36.8</ele>
    <time>2024-09-12T12:17:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6586050" lon="-5.2320080">
    <ele>36.8</ele>
    <time>2024-09-12T12:17:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6585460" lon="-5.2320220">
    <ele>36.8</ele>
    <time>2024-09-12T12:17:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6584920" lon="-5.2320330">
    <ele>36.8</ele>
    <time>2024-09-12T12:17:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6584280" lon="-5.2320450">
    <ele>37.0</ele>
    <time>2024-09-12T12:17:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6583740" lon="-5.2320570">
    <ele>36.8</ele>
    <time>2024-09-12T12:17:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6583150" lon="-5.2320760">
    <ele>36.8</ele>
    <time>2024-09-12T12:17:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6582560" lon="-5.2321030">
    <ele>36.8</ele>
    <time>2024-09-12T12:17:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6582030" lon="-5.2321390">
    <ele>36.6</ele>
    <time>2024-09-12T12:17:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6581440" lon="-5.2321790">
    <ele>36.4</ele>
    <time>2024-09-12T12:17:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6580850" lon="-5.2322200">
    <ele>36.2</ele>
    <time>2024-09-12T12:17:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>94</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6580200" lon="-5.2322630">
    <ele>36.0</ele>
    <time>2024-09-12T12:17:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6579560" lon="-5.2323050">
    <ele>35.6</ele>
    <time>2024-09-12T12:17:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6578860" lon="-5.2323410">
    <ele>35.2</ele>
    <time>2024-09-12T12:17:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6578110" lon="-5.2323710">
    <ele>34.8</ele>
    <time>2024-09-12T12:17:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6577310" lon="-5.2323940">
    <ele>34.4</ele>
    <time>2024-09-12T12:18:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6576450" lon="-5.2324070">
    <ele>34.0</ele>
    <time>2024-09-12T12:18:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6575640" lon="-5.2324080">
    <ele>33.4</ele>
    <time>2024-09-12T12:18:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6574730" lon="-5.2323970">
    <ele>33.0</ele>
    <time>2024-09-12T12:18:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6573820" lon="-5.2323720">
    <ele>32.6</ele>
    <time>2024-09-12T12:18:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6572910" lon="-5.2323270">
    <ele>32.0</ele>
    <time>2024-09-12T12:18:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>105</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6572000" lon="-5.2322700">
    <ele>31.6</ele>
    <time>2024-09-12T12:18:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>105</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6571080" lon="-5.2322070">
    <ele>31.2</ele>
    <time>2024-09-12T12:18:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6570170" lon="-5.2321440">
    <ele>30.8</ele>
    <time>2024-09-12T12:18:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6569210" lon="-5.2320850">
    <ele>30.4</ele>
    <time>2024-09-12T12:18:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6568190" lon="-5.2320420">
    <ele>30.0</ele>
    <time>2024-09-12T12:18:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>111</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6567220" lon="-5.2320180">
    <ele>29.8</ele>
    <time>2024-09-12T12:18:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6566150" lon="-5.2320110">
    <ele>29.6</ele>
    <time>2024-09-12T12:18:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6565130" lon="-5.2320140">
    <ele>29.4</ele>
    <time>2024-09-12T12:18:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>81</gpxtpx:watts>
      <gpxtpx:cad>110</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6564110" lon="-5.2320210">
    <ele>29.2</ele>
    <time>2024-09-12T12:18:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6563090" lon="-5.2320260">
    <ele>29.0</ele>
    <time>2024-09-12T12:18:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6562070" lon="-5.2320330">
    <ele>28.8</ele>
    <time>2024-09-12T12:18:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6561110" lon="-5.2320450">
    <ele>28.6</ele>
    <time>2024-09-12T12:18:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6560090" lon="-5.2320660">
    <ele>28.6</ele>
    <time>2024-09-12T12:18:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6559180" lon="-5.2320980">
    <ele>28.4</ele>
    <time>2024-09-12T12:18:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>107</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6558210" lon="-5.2321420">
    <ele>28.4</ele>
    <time>2024-09-12T12:18:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>105</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6557300" lon="-5.2322010">
    <ele>28.2</ele>
    <time>2024-09-12T12:18:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6556440" lon="-5.2322750">
    <ele>28.0</ele>
    <time>2024-09-12T12:18:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6555630" lon="-5.2323650">
    <ele>28.0</ele>
    <time>2024-09-12T12:18:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6554940" lon="-5.2324730">
    <ele>27.8</ele>
    <time>2024-09-12T12:18:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6554400" lon="-5.2326110">
    <ele>27.6</ele>
    <time>2024-09-12T12:18:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6554130" lon="-5.2327700">
    <ele>27.4</ele>
    <time>2024-09-12T12:18:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6554030" lon="-5.2329360">
    <ele>27.4</ele>
    <time>2024-09-12T12:18:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6554030" lon="-5.2331040">
    <ele>27.2</ele>
    <time>2024-09-12T12:18:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6554080" lon="-5.2332680">
    <ele>27.0</ele>
    <time>2024-09-12T12:18:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6554080" lon="-5.2334310">
    <ele>27.0</ele>
    <time>2024-09-12T12:18:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6553920" lon="-5.2335910">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6553490" lon="-5.2337370">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6552950" lon="-5.2338670">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6552420" lon="-5.2339860">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6551830" lon="-5.2340980">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>95</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6551180" lon="-5.2342010">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6550590" lon="-5.2342980">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6549950" lon="-5.2343920">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6549250" lon="-5.2344840">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6548660" lon="-5.2345760">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6548070" lon="-5.2346690">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6547480" lon="-5.2347600">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6546890" lon="-5.2348510">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6546300" lon="-5.2349400">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6545710" lon="-5.2350260">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6545170" lon="-5.2351070">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6544530" lon="-5.2351880">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>93</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6543990" lon="-5.2352670">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6543350" lon="-5.2353410">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>90</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6542760" lon="-5.2354020">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6542060" lon="-5.2354440">
    <ele>26.8</ele>
    <time>2024-09-12T12:18:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6541370" lon="-5.2354540">
    <ele>27.0</ele>
    <time>2024-09-12T12:18:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6540670" lon="-5.2354320">
    <ele>27.2</ele>
    <time>2024-09-12T12:18:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6540080" lon="-5.2353930">
    <ele>27.6</ele>
    <time>2024-09-12T12:18:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>87</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6539540" lon="-5.2353450">
    <ele>28.0</ele>
    <time>2024-09-12T12:18:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>68</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6539110" lon="-5.2352920">
    <ele>28.4</ele>
    <time>2024-09-12T12:18:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>127</gpxtpx:watts>
      <gpxtpx:cad>66</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6538680" lon="-5.2352360">
    <ele>28.8</ele>
    <time>2024-09-12T12:18:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>118</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6538410" lon="-5.2351800">
    <ele>29.2</ele>
    <time>2024-09-12T12:18:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>115</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6538090" lon="-5.2351270">
    <ele>29.6</ele>
    <time>2024-09-12T12:18:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>133</gpxtpx:watts>
      <gpxtpx:cad>59</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6537880" lon="-5.2350780">
    <ele>29.8</ele>
    <time>2024-09-12T12:19:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>145</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6537660" lon="-5.2350300">
    <ele>30.2</ele>
    <time>2024-09-12T12:19:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>137</gpxtpx:watts>
      <gpxtpx:cad>59</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6537400" lon="-5.2349860">
    <ele>30.4</ele>
    <time>2024-09-12T12:19:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>137</gpxtpx:watts>
      <gpxtpx:cad>55</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6537230" lon="-5.2349450">
    <ele>30.6</ele>
    <time>2024-09-12T12:19:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>121</gpxtpx:watts>
      <gpxtpx:cad>56</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6537070" lon="-5.2349080">
    <ele>30.8</ele>
    <time>2024-09-12T12:19:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>141</gpxtpx:watts>
      <gpxtpx:cad>58</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6536860" lon="-5.2348720">
    <ele>31.0</ele>
    <time>2024-09-12T12:19:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>129</gpxtpx:watts>
      <gpxtpx:cad>57</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6536750" lon="-5.2348400">
    <ele>31.2</ele>
    <time>2024-09-12T12:19:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>133</gpxtpx:watts>
      <gpxtpx:cad>58</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6536590" lon="-5.2348090">
    <ele>31.4</ele>
    <time>2024-09-12T12:19:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>144</gpxtpx:watts>
      <gpxtpx:cad>56</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6536430" lon="-5.2347790">
    <ele>31.6</ele>
    <time>2024-09-12T12:19:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>139</gpxtpx:watts>
      <gpxtpx:cad>57</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6536270" lon="-5.2347510">
    <ele>31.8</ele>
    <time>2024-09-12T12:19:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>139</gpxtpx:watts>
      <gpxtpx:cad>57</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6536110" lon="-5.2347240">
    <ele>32.0</ele>
    <time>2024-09-12T12:19:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>144</gpxtpx:watts>
      <gpxtpx:cad>58</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535950" lon="-5.2346980">
    <ele>32.2</ele>
    <time>2024-09-12T12:19:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>131</gpxtpx:watts>
      <gpxtpx:cad>55</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535790" lon="-5.2346750">
    <ele>32.4</ele>
    <time>2024-09-12T12:19:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>131</gpxtpx:watts>
      <gpxtpx:cad>51</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535680" lon="-5.2346530">
    <ele>32.6</ele>
    <time>2024-09-12T12:19:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>123</gpxtpx:watts>
      <gpxtpx:cad>52</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535520" lon="-5.2346340">
    <ele>32.8</ele>
    <time>2024-09-12T12:19:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>119</gpxtpx:watts>
      <gpxtpx:cad>53</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535360" lon="-5.2346170">
    <ele>33.0</ele>
    <time>2024-09-12T12:19:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>116</gpxtpx:watts>
      <gpxtpx:cad>52</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535140" lon="-5.2346020">
    <ele>33.2</ele>
    <time>2024-09-12T12:19:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>123</gpxtpx:watts>
      <gpxtpx:cad>49</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6535040" lon="-5.2345900">
    <ele>33.4</ele>
    <time>2024-09-12T12:19:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>116</gpxtpx:watts>
      <gpxtpx:cad>51</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6534870" lon="-5.2345790">
    <ele>33.4</ele>
    <time>2024-09-12T12:19:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>112</gpxtpx:watts>
      <gpxtpx:cad>47</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6534710" lon="-5.2345710">
    <ele>33.6</ele>
    <time>2024-09-12T12:19:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>108</gpxtpx:watts>
      <gpxtpx:cad>48</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6534550" lon="-5.2345650">
    <ele>33.8</ele>
    <time>2024-09-12T12:19:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>108</gpxtpx:watts>
      <gpxtpx:cad>48</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6534340" lon="-5.2345600">
    <ele>33.8</ele>
    <time>2024-09-12T12:19:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>116</gpxtpx:watts>
      <gpxtpx:cad>47</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6534230" lon="-5.2345580">
    <ele>34.0</ele>
    <time>2024-09-12T12:19:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>108</gpxtpx:watts>
      <gpxtpx:cad>49</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6534070" lon="-5.2345580">
    <ele>34.2</ele>
    <time>2024-09-12T12:19:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>100</gpxtpx:watts>
      <gpxtpx:cad>47</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6533860" lon="-5.2345600">
    <ele>34.2</ele>
    <time>2024-09-12T12:19:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>104</gpxtpx:watts>
      <gpxtpx:cad>46</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6533690" lon="-5.2345650">
    <ele>34.4</ele>
    <time>2024-09-12T12:19:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>96</gpxtpx:watts>
      <gpxtpx:cad>48</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6533530" lon="-5.2345710">
    <ele>34.6</ele>
    <time>2024-09-12T12:19:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>108</gpxtpx:watts>
      <gpxtpx:cad>45</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6533370" lon="-5.2345790">
    <ele>34.6</ele>
    <time>2024-09-12T12:19:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>96</gpxtpx:watts>
      <gpxtpx:cad>46</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6533210" lon="-5.2345890">
    <ele>34.8</ele>
    <time>2024-09-12T12:19:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>96</gpxtpx:watts>
      <gpxtpx:cad>46</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6533050" lon="-5.2346010">
    <ele>35.0</ele>
    <time>2024-09-12T12:19:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>96</gpxtpx:watts>
      <gpxtpx:cad>48</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6532890" lon="-5.2346140">
    <ele>35.0</ele>
    <time>2024-09-12T12:19:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>96</gpxtpx:watts>
      <gpxtpx:cad>47</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6532730" lon="-5.2346300">
    <ele>35.2</ele>
    <time>2024-09-12T12:19:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>100</gpxtpx:watts>
      <gpxtpx:cad>47</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6532570" lon="-5.2346480">
    <ele>35.2</ele>
    <time>2024-09-12T12:19:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>100</gpxtpx:watts>
      <gpxtpx:cad>46</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6532410" lon="-5.2346690">
    <ele>35.4</ele>
    <time>2024-09-12T12:19:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>108</gpxtpx:watts>
      <gpxtpx:cad>49</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6532250" lon="-5.2346900">
    <ele>35.4</ele>
    <time>2024-09-12T12:19:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>47</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6532080" lon="-5.2347130">
    <ele>35.6</ele>
    <time>2024-09-12T12:19:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>49</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531980" lon="-5.2347370">
    <ele>35.6</ele>
    <time>2024-09-12T12:19:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>51</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531820" lon="-5.2347610">
    <ele>35.8</ele>
    <time>2024-09-12T12:19:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>54</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531710" lon="-5.2347860">
    <ele>35.8</ele>
    <time>2024-09-12T12:19:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>54</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531600" lon="-5.2348100">
    <ele>36.0</ele>
    <time>2024-09-12T12:19:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>58</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531550" lon="-5.2348360">
    <ele>36.0</ele>
    <time>2024-09-12T12:19:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531440" lon="-5.2348620">
    <ele>36.0</ele>
    <time>2024-09-12T12:19:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>62</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531330" lon="-5.2348900">
    <ele>36.2</ele>
    <time>2024-09-12T12:19:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>63</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531170" lon="-5.2349200">
    <ele>36.2</ele>
    <time>2024-09-12T12:19:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>65</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531120" lon="-5.2349510">
    <ele>36.2</ele>
    <time>2024-09-12T12:19:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>64</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6531010" lon="-5.2349830">
    <ele>36.4</ele>
    <time>2024-09-12T12:19:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>67</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530900" lon="-5.2350150">
    <ele>36.4</ele>
    <time>2024-09-12T12:19:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530800" lon="-5.2350480">
    <ele>36.4</ele>
    <time>2024-09-12T12:19:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530690" lon="-5.2350820">
    <ele>36.6</ele>
    <time>2024-09-12T12:19:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530640" lon="-5.2351180">
    <ele>36.6</ele>
    <time>2024-09-12T12:19:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530530" lon="-5.2351540">
    <ele>36.6</ele>
    <time>2024-09-12T12:19:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530370" lon="-5.2351930">
    <ele>36.6</ele>
    <time>2024-09-12T12:19:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530310" lon="-5.2352310">
    <ele>36.8</ele>
    <time>2024-09-12T12:19:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530210" lon="-5.2352710">
    <ele>36.8</ele>
    <time>2024-09-12T12:19:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6530100" lon="-5.2353120">
    <ele>36.8</ele>
    <time>2024-09-12T12:19:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529990" lon="-5.2353540">
    <ele>36.8</ele>
    <time>2024-09-12T12:19:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529890" lon="-5.2353970">
    <ele>37.0</ele>
    <time>2024-09-12T12:19:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529720" lon="-5.2354400">
    <ele>37.0</ele>
    <time>2024-09-12T12:19:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529620" lon="-5.2354830">
    <ele>37.0</ele>
    <time>2024-09-12T12:19:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529460" lon="-5.2355260">
    <ele>37.0</ele>
    <time>2024-09-12T12:19:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529350" lon="-5.2355680">
    <ele>37.2</ele>
    <time>2024-09-12T12:20:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6529130" lon="-5.2356090">
    <ele>37.2</ele>
    <time>2024-09-12T12:20:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6528970" lon="-5.2356480">
    <ele>37.2</ele>
    <time>2024-09-12T12:20:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>69</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6528810" lon="-5.2356840">
    <ele>37.4</ele>
    <time>2024-09-12T12:20:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6528540" lon="-5.2357180">
    <ele>37.4</ele>
    <time>2024-09-12T12:20:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6528330" lon="-5.2357470">
    <ele>37.6</ele>
    <time>2024-09-12T12:20:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6528120" lon="-5.2357710">
    <ele>37.6</ele>
    <time>2024-09-12T12:20:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6527850" lon="-5.2357890">
    <ele>37.6</ele>
    <time>2024-09-12T12:20:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6527630" lon="-5.2358020">
    <ele>37.8</ele>
    <time>2024-09-12T12:20:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6527360" lon="-5.2358080">
    <ele>37.8</ele>
    <time>2024-09-12T12:20:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6527100" lon="-5.2358090">
    <ele>38.0</ele>
    <time>2024-09-12T12:20:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6526830" lon="-5.2358050">
    <ele>38.0</ele>
    <time>2024-09-12T12:20:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6526610" lon="-5.2357960">
    <ele>38.0</ele>
    <time>2024-09-12T12:20:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6526350" lon="-5.2357830">
    <ele>38.2</ele>
    <time>2024-09-12T12:20:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6526130" lon="-5.2357680">
    <ele>38.2</ele>
    <time>2024-09-12T12:20:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6525920" lon="-5.2357480">
    <ele>38.2</ele>
    <time>2024-09-12T12:20:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6525650" lon="-5.2357270">
    <ele>38.2</ele>
    <time>2024-09-12T12:20:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>69</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6525380" lon="-5.2357030">
    <ele>38.4</ele>
    <time>2024-09-12T12:20:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6525160" lon="-5.2356770">
    <ele>38.4</ele>
    <time>2024-09-12T12:20:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6524900" lon="-5.2356500">
    <ele>38.4</ele>
    <time>2024-09-12T12:20:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>69</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6524680" lon="-5.2356210">
    <ele>38.4</ele>
    <time>2024-09-12T12:20:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6524410" lon="-5.2355920">
    <ele>38.4</ele>
    <time>2024-09-12T12:20:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6524150" lon="-5.2355610">
    <ele>38.4</ele>
    <time>2024-09-12T12:20:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6523880" lon="-5.2355290">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6523610" lon="-5.2354970">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6523340" lon="-5.2354640">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6523020" lon="-5.2354320">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6522700" lon="-5.2354020">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6522380" lon="-5.2353760">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6522050" lon="-5.2353530">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6521680" lon="-5.2353380">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6521300" lon="-5.2353300">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520870" lon="-5.2353300">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520500" lon="-5.2353370">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520120" lon="-5.2353510">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519750" lon="-5.2353700">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519370" lon="-5.2353940">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519050" lon="-5.2354220">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6518620" lon="-5.2354560">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6518300" lon="-5.2354910">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517980" lon="-5.2355310">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517600" lon="-5.2355710">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517280" lon="-5.2356140">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6516900" lon="-5.2356590">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6516580" lon="-5.2357050">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6516260" lon="-5.2357510">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6515880" lon="-5.2357980">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6515510" lon="-5.2358460">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6515190" lon="-5.2358930">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6514810" lon="-5.2359380">
    <ele>39.0</ele>
    <time>2024-09-12T12:20:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6514380" lon="-5.2359800">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6513950" lon="-5.2360180">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>53</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6513470" lon="-5.2360500">
    <ele>38.8</ele>
    <time>2024-09-12T12:20:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>48</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6512990" lon="-5.2360730">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6512450" lon="-5.2360850">
    <ele>38.6</ele>
    <time>2024-09-12T12:20:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>86</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511970" lon="-5.2360780">
    <ele>38.4</ele>
    <time>2024-09-12T12:20:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>88</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511430" lon="-5.2360440">
    <ele>38.4</ele>
    <time>2024-09-12T12:20:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>89</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511000" lon="-5.2359860">
    <ele>38.2</ele>
    <time>2024-09-12T12:20:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>92</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6510570" lon="-5.2359110">
    <ele>38.0</ele>
    <time>2024-09-12T12:20:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>96</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6510200" lon="-5.2358220">
    <ele>37.8</ele>
    <time>2024-09-12T12:20:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509880" lon="-5.2357200">
    <ele>37.4</ele>
    <time>2024-09-12T12:21:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509660" lon="-5.2356060">
    <ele>37.2</ele>
    <time>2024-09-12T12:21:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509550" lon="-5.2354810">
    <ele>36.8</ele>
    <time>2024-09-12T12:21:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509720" lon="-5.2353510">
    <ele>36.4</ele>
    <time>2024-09-12T12:21:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6510140" lon="-5.2352360">
    <ele>36.2</ele>
    <time>2024-09-12T12:21:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6510730" lon="-5.2351410">
    <ele>36.0</ele>
    <time>2024-09-12T12:21:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>104</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511380" lon="-5.2350690">
    <ele>36.0</ele>
    <time>2024-09-12T12:21:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6512130" lon="-5.2350180">
    <ele>36.0</ele>
    <time>2024-09-12T12:21:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6512880" lon="-5.2349870">
    <ele>36.0</ele>
    <time>2024-09-12T12:21:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6513630" lon="-5.2349790">
    <ele>35.8</ele>
    <time>2024-09-12T12:21:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6514440" lon="-5.2349980">
    <ele>35.6</ele>
    <time>2024-09-12T12:21:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6515190" lon="-5.2350540">
    <ele>34.8</ele>
    <time>2024-09-12T12:21:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>102</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6515880" lon="-5.2351470">
    <ele>34.0</ele>
    <time>2024-09-12T12:21:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6516530" lon="-5.2352720">
    <ele>33.0</ele>
    <time>2024-09-12T12:21:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>103</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517060" lon="-5.2354240">
    <ele>32.0</ele>
    <time>2024-09-12T12:21:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517490" lon="-5.2355940">
    <ele>31.0</ele>
    <time>2024-09-12T12:21:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517870" lon="-5.2357770">
    <ele>29.8</ele>
    <time>2024-09-12T12:21:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6518240" lon="-5.2359690">
    <ele>28.8</ele>
    <time>2024-09-12T12:21:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6518670" lon="-5.2361670">
    <ele>28.0</ele>
    <time>2024-09-12T12:21:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519160" lon="-5.2363660">
    <ele>27.0</ele>
    <time>2024-09-12T12:21:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>106</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519690" lon="-5.2365680">
    <ele>26.0</ele>
    <time>2024-09-12T12:21:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>108</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520120" lon="-5.2367750">
    <ele>25.2</ele>
    <time>2024-09-12T12:21:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>109</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520500" lon="-5.2369910">
    <ele>24.6</ele>
    <time>2024-09-12T12:21:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>101</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520770" lon="-5.2372140">
    <ele>24.0</ele>
    <time>2024-09-12T12:21:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>99</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520770" lon="-5.2374410">
    <ele>23.6</ele>
    <time>2024-09-12T12:21:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>100</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520550" lon="-5.2376620">
    <ele>23.4</ele>
    <time>2024-09-12T12:21:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>98</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6520230" lon="-5.2378720">
    <ele>23.4</ele>
    <time>2024-09-12T12:21:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>70</gpxtpx:watts>
      <gpxtpx:cad>97</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519690" lon="-5.2380680">
    <ele>23.4</ele>
    <time>2024-09-12T12:21:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>91</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6519160" lon="-5.2382490">
    <ele>23.6</ele>
    <time>2024-09-12T12:21:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6518620" lon="-5.2384180">
    <ele>23.8</ele>
    <time>2024-09-12T12:21:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>87</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517980" lon="-5.2385740">
    <ele>24.2</ele>
    <time>2024-09-12T12:21:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>85</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6517390" lon="-5.2387190">
    <ele>24.4</ele>
    <time>2024-09-12T12:21:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>67</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6516740" lon="-5.2388530">
    <ele>24.8</ele>
    <time>2024-09-12T12:21:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6516150" lon="-5.2389760">
    <ele>25.2</ele>
    <time>2024-09-12T12:21:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6515510" lon="-5.2390900">
    <ele>25.4</ele>
    <time>2024-09-12T12:21:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>77</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6514920" lon="-5.2391960">
    <ele>25.8</ele>
    <time>2024-09-12T12:21:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6514330" lon="-5.2392950">
    <ele>26.2</ele>
    <time>2024-09-12T12:21:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6513740" lon="-5.2393860">
    <ele>26.6</ele>
    <time>2024-09-12T12:21:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6513200" lon="-5.2394720">
    <ele>26.8</ele>
    <time>2024-09-12T12:21:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6512720" lon="-5.2395520">
    <ele>27.2</ele>
    <time>2024-09-12T12:21:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6512290" lon="-5.2396290">
    <ele>27.4</ele>
    <time>2024-09-12T12:21:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511810" lon="-5.2397000">
    <ele>27.8</ele>
    <time>2024-09-12T12:21:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511380" lon="-5.2397680">
    <ele>28.0</ele>
    <time>2024-09-12T12:21:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6511000" lon="-5.2398320">
    <ele>28.2</ele>
    <time>2024-09-12T12:21:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6510630" lon="-5.2398920">
    <ele>28.4</ele>
    <time>2024-09-12T12:21:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6510310" lon="-5.2399500">
    <ele>28.6</ele>
    <time>2024-09-12T12:21:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509930" lon="-5.2400060">
    <ele>28.8</ele>
    <time>2024-09-12T12:21:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509660" lon="-5.2400580">
    <ele>29.0</ele>
    <time>2024-09-12T12:21:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509390" lon="-5.2401090">
    <ele>29.2</ele>
    <time>2024-09-12T12:21:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6509130" lon="-5.2401590">
    <ele>29.4</ele>
    <time>2024-09-12T12:21:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6508860" lon="-5.2402050">
    <ele>29.4</ele>
    <time>2024-09-12T12:21:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6508590" lon="-5.2402510">
    <ele>29.6</ele>
    <time>2024-09-12T12:21:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6508430" lon="-5.2402950">
    <ele>29.8</ele>
    <time>2024-09-12T12:21:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6508210" lon="-5.2403390">
    <ele>29.8</ele>
    <time>2024-09-12T12:21:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6508000" lon="-5.2403820">
    <ele>30.0</ele>
    <time>2024-09-12T12:21:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6507780" lon="-5.2404240">
    <ele>30.0</ele>
    <time>2024-09-12T12:21:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6507620" lon="-5.2404640">
    <ele>30.0</ele>
    <time>2024-09-12T12:21:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6507410" lon="-5.2405080">
    <ele>30.2</ele>
    <time>2024-09-12T12:21:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6507300" lon="-5.2405520">
    <ele>30.2</ele>
    <time>2024-09-12T12:21:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6507140" lon="-5.2405960">
    <ele>30.4</ele>
    <time>2024-09-12T12:21:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506980" lon="-5.2406420">
    <ele>30.4</ele>
    <time>2024-09-12T12:22:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506820" lon="-5.2406880">
    <ele>30.4</ele>
    <time>2024-09-12T12:22:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506710" lon="-5.2407360">
    <ele>30.6</ele>
    <time>2024-09-12T12:22:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506600" lon="-5.2407850">
    <ele>30.6</ele>
    <time>2024-09-12T12:22:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506500" lon="-5.2408340">
    <ele>30.6</ele>
    <time>2024-09-12T12:22:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506340" lon="-5.2408850">
    <ele>30.8</ele>
    <time>2024-09-12T12:22:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506280" lon="-5.2409360">
    <ele>30.8</ele>
    <time>2024-09-12T12:22:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506170" lon="-5.2409870">
    <ele>30.8</ele>
    <time>2024-09-12T12:22:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506070" lon="-5.2410390">
    <ele>30.8</ele>
    <time>2024-09-12T12:22:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6506010" lon="-5.2410920">
    <ele>30.8</ele>
    <time>2024-09-12T12:22:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505960" lon="-5.2411460">
    <ele>31.0</ele>
    <time>2024-09-12T12:22:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505850" lon="-5.2412000">
    <ele>31.0</ele>
    <time>2024-09-12T12:22:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505750" lon="-5.2412540">
    <ele>31.0</ele>
    <time>2024-09-12T12:22:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505690" lon="-5.2413100">
    <ele>31.0</ele>
    <time>2024-09-12T12:22:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505580" lon="-5.2413650">
    <ele>31.0</ele>
    <time>2024-09-12T12:22:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505530" lon="-5.2414210">
    <ele>31.2</ele>
    <time>2024-09-12T12:22:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505420" lon="-5.2414780">
    <ele>31.2</ele>
    <time>2024-09-12T12:22:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505370" lon="-5.2415350">
    <ele>31.2</ele>
    <time>2024-09-12T12:22:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505320" lon="-5.2415930">
    <ele>31.2</ele>
    <time>2024-09-12T12:22:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505210" lon="-5.2416510">
    <ele>31.2</ele>
    <time>2024-09-12T12:22:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505100" lon="-5.2417080">
    <ele>31.4</ele>
    <time>2024-09-12T12:22:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6505050" lon="-5.2417660">
    <ele>31.4</ele>
    <time>2024-09-12T12:22:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504890" lon="-5.2418230">
    <ele>31.4</ele>
    <time>2024-09-12T12:22:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504780" lon="-5.2418800">
    <ele>31.4</ele>
    <time>2024-09-12T12:22:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504670" lon="-5.2419360">
    <ele>31.6</ele>
    <time>2024-09-12T12:22:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504510" lon="-5.2419920">
    <ele>31.6</ele>
    <time>2024-09-12T12:22:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504350" lon="-5.2420460">
    <ele>31.6</ele>
    <time>2024-09-12T12:22:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504190" lon="-5.2420990">
    <ele>31.6</ele>
    <time>2024-09-12T12:22:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6504030" lon="-5.2421500">
    <ele>31.8</ele>
    <time>2024-09-12T12:22:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6503870" lon="-5.2421990">
    <ele>31.8</ele>
    <time>2024-09-12T12:22:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6503600" lon="-5.2422460">
    <ele>31.8</ele>
    <time>2024-09-12T12:22:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6503440" lon="-5.2422910">
    <ele>32.0</ele>
    <time>2024-09-12T12:22:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6503170" lon="-5.2423330">
    <ele>32.0</ele>
    <time>2024-09-12T12:22:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6502960" lon="-5.2423730">
    <ele>32.0</ele>
    <time>2024-09-12T12:22:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6502740" lon="-5.2424110">
    <ele>32.2</ele>
    <time>2024-09-12T12:22:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6502530" lon="-5.2424460">
    <ele>32.2</ele>
    <time>2024-09-12T12:22:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6502260" lon="-5.2424780">
    <ele>32.2</ele>
    <time>2024-09-12T12:22:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6501990" lon="-5.2425090">
    <ele>32.4</ele>
    <time>2024-09-12T12:22:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6501720" lon="-5.2425380">
    <ele>32.4</ele>
    <time>2024-09-12T12:22:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6501510" lon="-5.2425640">
    <ele>32.6</ele>
    <time>2024-09-12T12:22:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6501240" lon="-5.2425890">
    <ele>32.6</ele>
    <time>2024-09-12T12:22:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6501020" lon="-5.2426130">
    <ele>32.6</ele>
    <time>2024-09-12T12:22:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6500760" lon="-5.2426340">
    <ele>32.8</ele>
    <time>2024-09-12T12:22:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6500540" lon="-5.2426540">
    <ele>32.8</ele>
    <time>2024-09-12T12:22:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6500270" lon="-5.2426720">
    <ele>33.0</ele>
    <time>2024-09-12T12:22:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6500010" lon="-5.2426880">
    <ele>33.0</ele>
    <time>2024-09-12T12:22:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6499740" lon="-5.2427010">
    <ele>33.0</ele>
    <time>2024-09-12T12:22:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6499520" lon="-5.2427120">
    <ele>33.2</ele>
    <time>2024-09-12T12:22:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6499310" lon="-5.2427210">
    <ele>33.2</ele>
    <time>2024-09-12T12:22:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6499090" lon="-5.2427280">
    <ele>33.4</ele>
    <time>2024-09-12T12:22:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6498830" lon="-5.2427340">
    <ele>33.4</ele>
    <time>2024-09-12T12:22:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6498610" lon="-5.2427370">
    <ele>33.6</ele>
    <time>2024-09-12T12:22:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6498450" lon="-5.2427400">
    <ele>33.6</ele>
    <time>2024-09-12T12:22:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6498180" lon="-5.2427420">
    <ele>33.8</ele>
    <time>2024-09-12T12:22:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6498020" lon="-5.2427430">
    <ele>33.8</ele>
    <time>2024-09-12T12:22:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6497810" lon="-5.2427420">
    <ele>34.0</ele>
    <time>2024-09-12T12:22:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6497650" lon="-5.2427410">
    <ele>34.0</ele>
    <time>2024-09-12T12:22:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6497430" lon="-5.2427400">
    <ele>34.2</ele>
    <time>2024-09-12T12:22:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6497270" lon="-5.2427380">
    <ele>34.2</ele>
    <time>2024-09-12T12:22:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6497060" lon="-5.2427360">
    <ele>34.2</ele>
    <time>2024-09-12T12:22:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6496890" lon="-5.2427330">
    <ele>34.4</ele>
    <time>2024-09-12T12:23:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6496730" lon="-5.2427280">
    <ele>34.4</ele>
    <time>2024-09-12T12:23:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6496570" lon="-5.2427250">
    <ele>34.6</ele>
    <time>2024-09-12T12:23:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6496360" lon="-5.2427200">
    <ele>34.6</ele>
    <time>2024-09-12T12:23:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6496200" lon="-5.2427160">
    <ele>34.8</ele>
    <time>2024-09-12T12:23:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6496040" lon="-5.2427110">
    <ele>34.8</ele>
    <time>2024-09-12T12:23:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6495880" lon="-5.2427060">
    <ele>34.8</ele>
    <time>2024-09-12T12:23:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6495660" lon="-5.2427010">
    <ele>35.0</ele>
    <time>2024-09-12T12:23:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6495500" lon="-5.2426950">
    <ele>35.0</ele>
    <time>2024-09-12T12:23:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6495340" lon="-5.2426890">
    <ele>35.2</ele>
    <time>2024-09-12T12:23:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6495120" lon="-5.2426830">
    <ele>35.2</ele>
    <time>2024-09-12T12:23:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>82</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6494960" lon="-5.2426760">
    <ele>35.4</ele>
    <time>2024-09-12T12:23:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6494750" lon="-5.2426690">
    <ele>35.4</ele>
    <time>2024-09-12T12:23:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6494590" lon="-5.2426630">
    <ele>35.6</ele>
    <time>2024-09-12T12:23:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6494430" lon="-5.2426550">
    <ele>35.6</ele>
    <time>2024-09-12T12:23:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6494210" lon="-5.2426490">
    <ele>35.8</ele>
    <time>2024-09-12T12:23:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6494050" lon="-5.2426420">
    <ele>35.8</ele>
    <time>2024-09-12T12:23:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6493840" lon="-5.2426340">
    <ele>36.0</ele>
    <time>2024-09-12T12:23:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6493680" lon="-5.2426250">
    <ele>36.0</ele>
    <time>2024-09-12T12:23:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6493510" lon="-5.2426170">
    <ele>36.2</ele>
    <time>2024-09-12T12:23:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6493300" lon="-5.2426110">
    <ele>36.2</ele>
    <time>2024-09-12T12:23:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>82</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6493140" lon="-5.2426030">
    <ele>36.4</ele>
    <time>2024-09-12T12:23:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6492920" lon="-5.2425960">
    <ele>36.4</ele>
    <time>2024-09-12T12:23:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>82</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6492760" lon="-5.2425900">
    <ele>36.6</ele>
    <time>2024-09-12T12:23:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6492600" lon="-5.2425820">
    <ele>36.6</ele>
    <time>2024-09-12T12:23:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>84</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6492390" lon="-5.2425750">
    <ele>36.8</ele>
    <time>2024-09-12T12:23:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6492230" lon="-5.2425680">
    <ele>36.8</ele>
    <time>2024-09-12T12:23:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>80</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6492010" lon="-5.2425620">
    <ele>37.0</ele>
    <time>2024-09-12T12:23:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6491850" lon="-5.2425550">
    <ele>37.0</ele>
    <time>2024-09-12T12:23:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6491690" lon="-5.2425480">
    <ele>37.2</ele>
    <time>2024-09-12T12:23:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6491480" lon="-5.2425420">
    <ele>37.2</ele>
    <time>2024-09-12T12:23:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>78</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6491320" lon="-5.2425360">
    <ele>37.4</ele>
    <time>2024-09-12T12:23:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>76</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6491100" lon="-5.2425300">
    <ele>37.4</ele>
    <time>2024-09-12T12:23:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6490940" lon="-5.2425250">
    <ele>37.6</ele>
    <time>2024-09-12T12:23:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6490780" lon="-5.2425200">
    <ele>37.6</ele>
    <time>2024-09-12T12:23:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6490560" lon="-5.2425160">
    <ele>37.6</ele>
    <time>2024-09-12T12:23:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6490400" lon="-5.2425120">
    <ele>37.8</ele>
    <time>2024-09-12T12:23:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6490240" lon="-5.2425090">
    <ele>37.8</ele>
    <time>2024-09-12T12:23:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6490080" lon="-5.2425050">
    <ele>38.0</ele>
    <time>2024-09-12T12:23:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6489870" lon="-5.2425020">
    <ele>38.0</ele>
    <time>2024-09-12T12:23:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6489710" lon="-5.2425000">
    <ele>38.2</ele>
    <time>2024-09-12T12:23:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6489550" lon="-5.2424990">
    <ele>38.2</ele>
    <time>2024-09-12T12:23:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6489330" lon="-5.2424970">
    <ele>38.4</ele>
    <time>2024-09-12T12:23:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6489170" lon="-5.2424960">
    <ele>38.4</ele>
    <time>2024-09-12T12:23:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6489010" lon="-5.2424960">
    <ele>38.4</ele>
    <time>2024-09-12T12:23:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6488790" lon="-5.2424970">
    <ele>38.6</ele>
    <time>2024-09-12T12:23:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6488690" lon="-5.2424980">
    <ele>38.6</ele>
    <time>2024-09-12T12:23:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6488470" lon="-5.2425000">
    <ele>38.8</ele>
    <time>2024-09-12T12:23:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6488260" lon="-5.2425030">
    <ele>38.8</ele>
    <time>2024-09-12T12:23:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6488100" lon="-5.2425060">
    <ele>39.0</ele>
    <time>2024-09-12T12:23:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6487940" lon="-5.2425100">
    <ele>39.0</ele>
    <time>2024-09-12T12:23:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6487720" lon="-5.2425150">
    <ele>39.0</ele>
    <time>2024-09-12T12:23:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>73</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6487560" lon="-5.2425210">
    <ele>39.2</ele>
    <time>2024-09-12T12:23:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6487350" lon="-5.2425280">
    <ele>39.2</ele>
    <time>2024-09-12T12:23:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6487180" lon="-5.2425360">
    <ele>39.4</ele>
    <time>2024-09-12T12:23:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6487020" lon="-5.2425440">
    <ele>39.4</ele>
    <time>2024-09-12T12:23:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6486810" lon="-5.2425530">
    <ele>39.6</ele>
    <time>2024-09-12T12:23:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6486650" lon="-5.2425630">
    <ele>39.6</ele>
    <time>2024-09-12T12:23:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6486490" lon="-5.2425740">
    <ele>39.6</ele>
    <time>2024-09-12T12:23:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6486270" lon="-5.2425860">
    <ele>39.8</ele>
    <time>2024-09-12T12:23:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6486110" lon="-5.2425980">
    <ele>39.8</ele>
    <time>2024-09-12T12:24:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>71</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485950" lon="-5.2426120">
    <ele>40.0</ele>
    <time>2024-09-12T12:24:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485740" lon="-5.2426240">
    <ele>40.0</ele>
    <time>2024-09-12T12:24:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485630" lon="-5.2426380">
    <ele>40.0</ele>
    <time>2024-09-12T12:24:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485470" lon="-5.2426510">
    <ele>40.2</ele>
    <time>2024-09-12T12:24:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485310" lon="-5.2426650">
    <ele>40.2</ele>
    <time>2024-09-12T12:24:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6485150" lon="-5.2426790">
    <ele>40.2</ele>
    <time>2024-09-12T12:24:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484990" lon="-5.2426940">
    <ele>40.4</ele>
    <time>2024-09-12T12:24:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484820" lon="-5.2427080">
    <ele>40.4</ele>
    <time>2024-09-12T12:24:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484720" lon="-5.2427240">
    <ele>40.4</ele>
    <time>2024-09-12T12:24:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484560" lon="-5.2427400">
    <ele>40.6</ele>
    <time>2024-09-12T12:24:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484450" lon="-5.2427570">
    <ele>40.6</ele>
    <time>2024-09-12T12:24:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484290" lon="-5.2427740">
    <ele>40.6</ele>
    <time>2024-09-12T12:24:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484130" lon="-5.2427920">
    <ele>40.8</ele>
    <time>2024-09-12T12:24:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6484020" lon="-5.2428110">
    <ele>40.8</ele>
    <time>2024-09-12T12:24:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483860" lon="-5.2428300">
    <ele>40.8</ele>
    <time>2024-09-12T12:24:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483700" lon="-5.2428500">
    <ele>41.0</ele>
    <time>2024-09-12T12:24:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483540" lon="-5.2428700">
    <ele>41.0</ele>
    <time>2024-09-12T12:24:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483430" lon="-5.2428910">
    <ele>41.0</ele>
    <time>2024-09-12T12:24:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483270" lon="-5.2429130">
    <ele>41.2</ele>
    <time>2024-09-12T12:24:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483110" lon="-5.2429360">
    <ele>41.2</ele>
    <time>2024-09-12T12:24:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6483000" lon="-5.2429590">
    <ele>41.2</ele>
    <time>2024-09-12T12:24:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482840" lon="-5.2429830">
    <ele>41.4</ele>
    <time>2024-09-12T12:24:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482730" lon="-5.2430080">
    <ele>41.4</ele>
    <time>2024-09-12T12:24:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482570" lon="-5.2430340">
    <ele>41.4</ele>
    <time>2024-09-12T12:24:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482410" lon="-5.2430600">
    <ele>41.6</ele>
    <time>2024-09-12T12:24:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482300" lon="-5.2430870">
    <ele>41.6</ele>
    <time>2024-09-12T12:24:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6482140" lon="-5.2431150">
    <ele>41.6</ele>
    <time>2024-09-12T12:24:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481980" lon="-5.2431440">
    <ele>41.6</ele>
    <time>2024-09-12T12:24:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481870" lon="-5.2431740">
    <ele>41.8</ele>
    <time>2024-09-12T12:24:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481710" lon="-5.2432040">
    <ele>41.8</ele>
    <time>2024-09-12T12:24:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481610" lon="-5.2432360">
    <ele>41.8</ele>
    <time>2024-09-12T12:24:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481440" lon="-5.2432690">
    <ele>42.0</ele>
    <time>2024-09-12T12:24:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481340" lon="-5.2433020">
    <ele>42.0</ele>
    <time>2024-09-12T12:24:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481180" lon="-5.2433360">
    <ele>42.0</ele>
    <time>2024-09-12T12:24:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6481070" lon="-5.2433720">
    <ele>42.0</ele>
    <time>2024-09-12T12:24:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480910" lon="-5.2434080">
    <ele>42.2</ele>
    <time>2024-09-12T12:24:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480800" lon="-5.2434450">
    <ele>42.2</ele>
    <time>2024-09-12T12:24:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480640" lon="-5.2434820">
    <ele>42.2</ele>
    <time>2024-09-12T12:24:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>49</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480530" lon="-5.2435200">
    <ele>42.2</ele>
    <time>2024-09-12T12:24:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480370" lon="-5.2435590">
    <ele>42.4</ele>
    <time>2024-09-12T12:24:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480260" lon="-5.2435990">
    <ele>42.4</ele>
    <time>2024-09-12T12:24:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480160" lon="-5.2436380">
    <ele>42.4</ele>
    <time>2024-09-12T12:24:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6480000" lon="-5.2436800">
    <ele>42.4</ele>
    <time>2024-09-12T12:24:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479890" lon="-5.2437200">
    <ele>42.4</ele>
    <time>2024-09-12T12:24:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479730" lon="-5.2437620">
    <ele>42.6</ele>
    <time>2024-09-12T12:24:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>53</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479570" lon="-5.2438040">
    <ele>42.6</ele>
    <time>2024-09-12T12:24:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479460" lon="-5.2438460">
    <ele>42.6</ele>
    <time>2024-09-12T12:24:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479300" lon="-5.2438880">
    <ele>42.6</ele>
    <time>2024-09-12T12:24:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479140" lon="-5.2439300">
    <ele>42.8</ele>
    <time>2024-09-12T12:24:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6479030" lon="-5.2439720">
    <ele>42.8</ele>
    <time>2024-09-12T12:24:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6478820" lon="-5.2440140">
    <ele>42.8</ele>
    <time>2024-09-12T12:24:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6478660" lon="-5.2440550">
    <ele>42.8</ele>
    <time>2024-09-12T12:24:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6478490" lon="-5.2440940">
    <ele>42.8</ele>
    <time>2024-09-12T12:24:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>53</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6478280" lon="-5.2441340">
    <ele>43.0</ele>
    <time>2024-09-12T12:24:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6478120" lon="-5.2441710">
    <ele>43.0</ele>
    <time>2024-09-12T12:24:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6477850" lon="-5.2442070">
    <ele>43.0</ele>
    <time>2024-09-12T12:24:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6477640" lon="-5.2442420">
    <ele>43.2</ele>
    <time>2024-09-12T12:24:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6477420" lon="-5.2442750">
    <ele>43.2</ele>
    <time>2024-09-12T12:24:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>53</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6477150" lon="-5.2443030">
    <ele>43.2</ele>
    <time>2024-09-12T12:24:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6476890" lon="-5.2443310">
    <ele>43.2</ele>
    <time>2024-09-12T12:25:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6476670" lon="-5.2443570">
    <ele>43.4</ele>
    <time>2024-09-12T12:25:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>53</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6476400" lon="-5.2443820">
    <ele>43.4</ele>
    <time>2024-09-12T12:25:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6476130" lon="-5.2444050">
    <ele>43.4</ele>
    <time>2024-09-12T12:25:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6475870" lon="-5.2444250">
    <ele>43.6</ele>
    <time>2024-09-12T12:25:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6475600" lon="-5.2444430">
    <ele>43.6</ele>
    <time>2024-09-12T12:25:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6475330" lon="-5.2444600">
    <ele>43.6</ele>
    <time>2024-09-12T12:25:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6475060" lon="-5.2444750">
    <ele>43.8</ele>
    <time>2024-09-12T12:25:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6474790" lon="-5.2444880">
    <ele>43.8</ele>
    <time>2024-09-12T12:25:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6474520" lon="-5.2445000">
    <ele>43.8</ele>
    <time>2024-09-12T12:25:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6474260" lon="-5.2445110">
    <ele>44.0</ele>
    <time>2024-09-12T12:25:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6473990" lon="-5.2445190">
    <ele>44.0</ele>
    <time>2024-09-12T12:25:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6473720" lon="-5.2445270">
    <ele>44.0</ele>
    <time>2024-09-12T12:25:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6473450" lon="-5.2445340">
    <ele>44.0</ele>
    <time>2024-09-12T12:25:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6473180" lon="-5.2445390">
    <ele>44.2</ele>
    <time>2024-09-12T12:25:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6472920" lon="-5.2445420">
    <ele>44.2</ele>
    <time>2024-09-12T12:25:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>53</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6472650" lon="-5.2445430">
    <ele>44.2</ele>
    <time>2024-09-12T12:25:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6472380" lon="-5.2445420">
    <ele>44.4</ele>
    <time>2024-09-12T12:25:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6472110" lon="-5.2445370">
    <ele>44.4</ele>
    <time>2024-09-12T12:25:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6471840" lon="-5.2445310">
    <ele>44.4</ele>
    <time>2024-09-12T12:25:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6471570" lon="-5.2445230">
    <ele>44.4</ele>
    <time>2024-09-12T12:25:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6471310" lon="-5.2445130">
    <ele>44.6</ele>
    <time>2024-09-12T12:25:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6471040" lon="-5.2445000">
    <ele>44.6</ele>
    <time>2024-09-12T12:25:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6470770" lon="-5.2444850">
    <ele>44.6</ele>
    <time>2024-09-12T12:25:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6470560" lon="-5.2444670">
    <ele>44.6</ele>
    <time>2024-09-12T12:25:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6470230" lon="-5.2444480">
    <ele>44.8</ele>
    <time>2024-09-12T12:25:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6470020" lon="-5.2444250">
    <ele>44.8</ele>
    <time>2024-09-12T12:25:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6469750" lon="-5.2444020">
    <ele>44.8</ele>
    <time>2024-09-12T12:25:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6469480" lon="-5.2443750">
    <ele>44.8</ele>
    <time>2024-09-12T12:25:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6469210" lon="-5.2443470">
    <ele>44.8</ele>
    <time>2024-09-12T12:25:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6468950" lon="-5.2443170">
    <ele>44.8</ele>
    <time>2024-09-12T12:25:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6468730" lon="-5.2442850">
    <ele>44.8</ele>
    <time>2024-09-12T12:25:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6468460" lon="-5.2442510">
    <ele>45.0</ele>
    <time>2024-09-12T12:25:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6468190" lon="-5.2442160">
    <ele>45.0</ele>
    <time>2024-09-12T12:25:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6467930" lon="-5.2441790">
    <ele>45.0</ele>
    <time>2024-09-12T12:25:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6467660" lon="-5.2441410">
    <ele>45.0</ele>
    <time>2024-09-12T12:25:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6467390" lon="-5.2441020">
    <ele>45.0</ele>
    <time>2024-09-12T12:25:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6467120" lon="-5.2440610">
    <ele>45.0</ele>
    <time>2024-09-12T12:25:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6466910" lon="-5.2440190">
    <ele>45.0</ele>
    <time>2024-09-12T12:25:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6466640" lon="-5.2439760">
    <ele>45.2</ele>
    <time>2024-09-12T12:25:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6466370" lon="-5.2439330">
    <ele>45.2</ele>
    <time>2024-09-12T12:25:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6466100" lon="-5.2438880">
    <ele>45.2</ele>
    <time>2024-09-12T12:25:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6465890" lon="-5.2438430">
    <ele>45.2</ele>
    <time>2024-09-12T12:25:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6465620" lon="-5.2437970">
    <ele>45.2</ele>
    <time>2024-09-12T12:25:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6465350" lon="-5.2437510">
    <ele>45.2</ele>
    <time>2024-09-12T12:25:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6465080" lon="-5.2437050">
    <ele>45.4</ele>
    <time>2024-09-12T12:25:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464870" lon="-5.2436580">
    <ele>45.4</ele>
    <time>2024-09-12T12:25:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464600" lon="-5.2436110">
    <ele>45.4</ele>
    <time>2024-09-12T12:25:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464330" lon="-5.2435650">
    <ele>45.4</ele>
    <time>2024-09-12T12:25:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6464060" lon="-5.2435180">
    <ele>45.4</ele>
    <time>2024-09-12T12:25:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6463850" lon="-5.2434720">
    <ele>45.6</ele>
    <time>2024-09-12T12:25:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6463580" lon="-5.2434250">
    <ele>45.6</ele>
    <time>2024-09-12T12:25:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6463310" lon="-5.2433790">
    <ele>45.6</ele>
    <time>2024-09-12T12:25:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6463040" lon="-5.2433330">
    <ele>45.8</ele>
    <time>2024-09-12T12:25:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6462780" lon="-5.2432870">
    <ele>45.8</ele>
    <time>2024-09-12T12:25:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6462510" lon="-5.2432430">
    <ele>45.8</ele>
    <time>2024-09-12T12:25:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6462240" lon="-5.2431980">
    <ele>45.8</ele>
    <time>2024-09-12T12:25:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6462030" lon="-5.2431540">
    <ele>46.0</ele>
    <time>2024-09-12T12:25:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6461760" lon="-5.2431100">
    <ele>46.0</ele>
    <time>2024-09-12T12:25:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6461490" lon="-5.2430680">
    <ele>46.0</ele>
    <time>2024-09-12T12:25:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6461220" lon="-5.2430250">
    <ele>46.2</ele>
    <time>2024-09-12T12:26:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6461010" lon="-5.2429830">
    <ele>46.2</ele>
    <time>2024-09-12T12:26:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6460740" lon="-5.2429420">
    <ele>46.2</ele>
    <time>2024-09-12T12:26:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6460470" lon="-5.2429020">
    <ele>46.4</ele>
    <time>2024-09-12T12:26:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6460200" lon="-5.2428620">
    <ele>46.4</ele>
    <time>2024-09-12T12:26:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6459930" lon="-5.2428230">
    <ele>46.6</ele>
    <time>2024-09-12T12:26:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6459670" lon="-5.2427850">
    <ele>46.6</ele>
    <time>2024-09-12T12:26:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6459450" lon="-5.2427480">
    <ele>46.6</ele>
    <time>2024-09-12T12:26:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6459180" lon="-5.2427120">
    <ele>46.8</ele>
    <time>2024-09-12T12:26:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6458910" lon="-5.2426770">
    <ele>46.8</ele>
    <time>2024-09-12T12:26:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6458650" lon="-5.2426430">
    <ele>47.0</ele>
    <time>2024-09-12T12:26:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6458430" lon="-5.2426110">
    <ele>47.0</ele>
    <time>2024-09-12T12:26:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6458160" lon="-5.2425790">
    <ele>47.2</ele>
    <time>2024-09-12T12:26:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6457900" lon="-5.2425480">
    <ele>47.2</ele>
    <time>2024-09-12T12:26:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6457630" lon="-5.2425190">
    <ele>47.2</ele>
    <time>2024-09-12T12:26:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6457410" lon="-5.2424900">
    <ele>47.4</ele>
    <time>2024-09-12T12:26:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6457140" lon="-5.2424620">
    <ele>47.4</ele>
    <time>2024-09-12T12:26:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6456930" lon="-5.2424350">
    <ele>47.6</ele>
    <time>2024-09-12T12:26:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6456710" lon="-5.2424090">
    <ele>47.6</ele>
    <time>2024-09-12T12:26:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6456450" lon="-5.2423840">
    <ele>47.8</ele>
    <time>2024-09-12T12:26:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>68</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6456230" lon="-5.2423580">
    <ele>47.8</ele>
    <time>2024-09-12T12:26:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6456020" lon="-5.2423320">
    <ele>48.0</ele>
    <time>2024-09-12T12:26:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6455800" lon="-5.2423050">
    <ele>48.0</ele>
    <time>2024-09-12T12:26:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6455530" lon="-5.2422820">
    <ele>48.0</ele>
    <time>2024-09-12T12:26:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6455370" lon="-5.2422610">
    <ele>48.2</ele>
    <time>2024-09-12T12:26:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6455110" lon="-5.2422380">
    <ele>48.2</ele>
    <time>2024-09-12T12:26:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6454890" lon="-5.2422160">
    <ele>48.2</ele>
    <time>2024-09-12T12:26:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6454680" lon="-5.2421940">
    <ele>48.4</ele>
    <time>2024-09-12T12:26:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6454460" lon="-5.2421710">
    <ele>48.4</ele>
    <time>2024-09-12T12:26:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>61</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6454190" lon="-5.2421490">
    <ele>48.4</ele>
    <time>2024-09-12T12:26:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>72</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6453980" lon="-5.2421270">
    <ele>48.6</ele>
    <time>2024-09-12T12:26:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6453760" lon="-5.2421040">
    <ele>48.6</ele>
    <time>2024-09-12T12:26:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6453550" lon="-5.2420810">
    <ele>48.6</ele>
    <time>2024-09-12T12:26:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6453280" lon="-5.2420580">
    <ele>48.8</ele>
    <time>2024-09-12T12:26:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>64</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6453070" lon="-5.2420360">
    <ele>48.8</ele>
    <time>2024-09-12T12:26:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452850" lon="-5.2420130">
    <ele>48.8</ele>
    <time>2024-09-12T12:26:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452640" lon="-5.2419900">
    <ele>49.0</ele>
    <time>2024-09-12T12:26:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452420" lon="-5.2419670">
    <ele>49.0</ele>
    <time>2024-09-12T12:26:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6452210" lon="-5.2419430">
    <ele>49.0</ele>
    <time>2024-09-12T12:26:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451940" lon="-5.2419210">
    <ele>49.2</ele>
    <time>2024-09-12T12:26:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451730" lon="-5.2418970">
    <ele>49.2</ele>
    <time>2024-09-12T12:26:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451510" lon="-5.2418730">
    <ele>49.2</ele>
    <time>2024-09-12T12:26:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451300" lon="-5.2418480">
    <ele>49.4</ele>
    <time>2024-09-12T12:26:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6451030" lon="-5.2418240">
    <ele>49.4</ele>
    <time>2024-09-12T12:26:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>69</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450760" lon="-5.2417980">
    <ele>49.4</ele>
    <time>2024-09-12T12:26:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450490" lon="-5.2417720">
    <ele>49.4</ele>
    <time>2024-09-12T12:26:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450280" lon="-5.2417470">
    <ele>49.6</ele>
    <time>2024-09-12T12:26:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>47</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6450010" lon="-5.2417200">
    <ele>49.6</ele>
    <time>2024-09-12T12:26:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449790" lon="-5.2416950">
    <ele>49.6</ele>
    <time>2024-09-12T12:26:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449530" lon="-5.2416690">
    <ele>49.6</ele>
    <time>2024-09-12T12:26:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449310" lon="-5.2416430">
    <ele>49.8</ele>
    <time>2024-09-12T12:26:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6449040" lon="-5.2416170">
    <ele>49.8</ele>
    <time>2024-09-12T12:26:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6448780" lon="-5.2415910">
    <ele>49.8</ele>
    <time>2024-09-12T12:26:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6448510" lon="-5.2415650">
    <ele>50.0</ele>
    <time>2024-09-12T12:26:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6448240" lon="-5.2415390">
    <ele>50.0</ele>
    <time>2024-09-12T12:26:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6448020" lon="-5.2415130">
    <ele>50.0</ele>
    <time>2024-09-12T12:26:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6447760" lon="-5.2414860">
    <ele>50.0</ele>
    <time>2024-09-12T12:26:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6447490" lon="-5.2414590">
    <ele>50.2</ele>
    <time>2024-09-12T12:26:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6447220" lon="-5.2414320">
    <ele>50.2</ele>
    <time>2024-09-12T12:26:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6447010" lon="-5.2414060">
    <ele>50.2</ele>
    <time>2024-09-12T12:26:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6446740" lon="-5.2413780">
    <ele>50.2</ele>
    <time>2024-09-12T12:27:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6446470" lon="-5.2413510">
    <ele>50.4</ele>
    <time>2024-09-12T12:27:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6446200" lon="-5.2413240">
    <ele>50.4</ele>
    <time>2024-09-12T12:27:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6445930" lon="-5.2412960">
    <ele>50.4</ele>
    <time>2024-09-12T12:27:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6445660" lon="-5.2412690">
    <ele>50.4</ele>
    <time>2024-09-12T12:27:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6445400" lon="-5.2412410">
    <ele>50.6</ele>
    <time>2024-09-12T12:27:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6445130" lon="-5.2412130">
    <ele>50.6</ele>
    <time>2024-09-12T12:27:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444860" lon="-5.2411860">
    <ele>50.6</ele>
    <time>2024-09-12T12:27:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444590" lon="-5.2411580">
    <ele>50.8</ele>
    <time>2024-09-12T12:27:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444320" lon="-5.2411300">
    <ele>50.8</ele>
    <time>2024-09-12T12:27:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6444050" lon="-5.2411020">
    <ele>50.8</ele>
    <time>2024-09-12T12:27:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6443790" lon="-5.2410740">
    <ele>50.8</ele>
    <time>2024-09-12T12:27:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6443520" lon="-5.2410460">
    <ele>51.0</ele>
    <time>2024-09-12T12:27:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6443250" lon="-5.2410180">
    <ele>51.0</ele>
    <time>2024-09-12T12:27:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6442980" lon="-5.2409900">
    <ele>51.0</ele>
    <time>2024-09-12T12:27:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>59</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6442710" lon="-5.2409620">
    <ele>51.0</ele>
    <time>2024-09-12T12:27:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6442450" lon="-5.2409330">
    <ele>51.2</ele>
    <time>2024-09-12T12:27:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6442180" lon="-5.2409040">
    <ele>51.2</ele>
    <time>2024-09-12T12:27:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6441910" lon="-5.2408740">
    <ele>51.2</ele>
    <time>2024-09-12T12:27:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>74</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6441640" lon="-5.2408460">
    <ele>51.2</ele>
    <time>2024-09-12T12:27:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>48</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6441370" lon="-5.2408180">
    <ele>51.4</ele>
    <time>2024-09-12T12:27:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6441050" lon="-5.2407910">
    <ele>51.4</ele>
    <time>2024-09-12T12:27:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6440780" lon="-5.2407630">
    <ele>51.4</ele>
    <time>2024-09-12T12:27:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6440510" lon="-5.2407360">
    <ele>51.6</ele>
    <time>2024-09-12T12:27:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6440250" lon="-5.2407080">
    <ele>51.6</ele>
    <time>2024-09-12T12:27:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>66</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6439980" lon="-5.2406780">
    <ele>51.6</ele>
    <time>2024-09-12T12:27:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6439760" lon="-5.2406490">
    <ele>51.8</ele>
    <time>2024-09-12T12:27:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6439550" lon="-5.2406170">
    <ele>51.8</ele>
    <time>2024-09-12T12:27:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6439280" lon="-5.2405850">
    <ele>52.0</ele>
    <time>2024-09-12T12:27:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>65</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6439070" lon="-5.2405520">
    <ele>52.0</ele>
    <time>2024-09-12T12:27:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6438850" lon="-5.2405190">
    <ele>52.0</ele>
    <time>2024-09-12T12:27:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6438640" lon="-5.2404840">
    <ele>52.2</ele>
    <time>2024-09-12T12:27:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6438480" lon="-5.2404490">
    <ele>52.2</ele>
    <time>2024-09-12T12:27:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6438310" lon="-5.2404130">
    <ele>52.4</ele>
    <time>2024-09-12T12:27:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>63</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6438150" lon="-5.2403770">
    <ele>52.4</ele>
    <time>2024-09-12T12:27:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437990" lon="-5.2403410">
    <ele>52.6</ele>
    <time>2024-09-12T12:27:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>62</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437890" lon="-5.2403050">
    <ele>52.6</ele>
    <time>2024-09-12T12:27:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>79</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437830" lon="-5.2402680">
    <ele>52.8</ele>
    <time>2024-09-12T12:27:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437670" lon="-5.2402310">
    <ele>52.8</ele>
    <time>2024-09-12T12:27:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437620" lon="-5.2401930">
    <ele>53.0</ele>
    <time>2024-09-12T12:27:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437560" lon="-5.2401550">
    <ele>53.0</ele>
    <time>2024-09-12T12:27:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437510" lon="-5.2401170">
    <ele>53.2</ele>
    <time>2024-09-12T12:27:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437400" lon="-5.2400790">
    <ele>53.2</ele>
    <time>2024-09-12T12:27:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437400" lon="-5.2400400">
    <ele>53.2</ele>
    <time>2024-09-12T12:27:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>75</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437300" lon="-5.2399990">
    <ele>53.4</ele>
    <time>2024-09-12T12:27:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437300" lon="-5.2399580">
    <ele>53.4</ele>
    <time>2024-09-12T12:27:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437190" lon="-5.2399160">
    <ele>53.4</ele>
    <time>2024-09-12T12:27:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437130" lon="-5.2398720">
    <ele>53.4</ele>
    <time>2024-09-12T12:27:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6437030" lon="-5.2398280">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>72</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6436920" lon="-5.2397820">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>74</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6436760" lon="-5.2397370">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>71</gpxtpx:watts>
      <gpxtpx:cad>75</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6436600" lon="-5.2396910">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>48</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6436380" lon="-5.2396470">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6436170" lon="-5.2396040">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:53Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6435900" lon="-5.2395660">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:54Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6435630" lon="-5.2395320">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:55Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6435310" lon="-5.2395030">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:56Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6434990" lon="-5.2394780">
    <ele>53.6</ele>
    <time>2024-09-12T12:27:57Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6434670" lon="-5.2394580">
    <ele>53.8</ele>
    <time>2024-09-12T12:27:58Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>58</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6434290" lon="-5.2394420">
    <ele>53.8</ele>
    <time>2024-09-12T12:27:59Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>60</gpxtpx:watts>
      <gpxtpx:cad>84</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6433920" lon="-5.2394300">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:00Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>57</gpxtpx:watts>
      <gpxtpx:cad>83</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6433540" lon="-5.2394220">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:01Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6433220" lon="-5.2394160">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:02Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6432790" lon="-5.2394130">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:03Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6432410" lon="-5.2394130">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:04Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6432040" lon="-5.2394140">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:05Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6431610" lon="-5.2394160">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:06Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6431180" lon="-5.2394190">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:07Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6430750" lon="-5.2394220">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:08Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6430320" lon="-5.2394250">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:09Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6429890" lon="-5.2394280">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:10Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6429520" lon="-5.2394300">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:11Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6429030" lon="-5.2394320">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:12Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6428610" lon="-5.2394330">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:13Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6428180" lon="-5.2394300">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:14Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6427690" lon="-5.2394310">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:15Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6427260" lon="-5.2394320">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:16Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6426780" lon="-5.2394340">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:17Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>51</gpxtpx:watts>
      <gpxtpx:cad>77</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6426350" lon="-5.2394350">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:18Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6425870" lon="-5.2394360">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:19Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6425390" lon="-5.2394380">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:20Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>56</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6424900" lon="-5.2394390">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:21Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>54</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6424420" lon="-5.2394390">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:22Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6423940" lon="-5.2394400">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:23Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6423460" lon="-5.2394390">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:24Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6422970" lon="-5.2394390">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:25Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6422490" lon="-5.2394380">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:26Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>82</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6422010" lon="-5.2394360">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:27Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>81</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6421520" lon="-5.2394340">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:28Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>55</gpxtpx:watts>
      <gpxtpx:cad>80</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6421040" lon="-5.2394320">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:29Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>79</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6420510" lon="-5.2394320">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:30Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>52</gpxtpx:watts>
      <gpxtpx:cad>78</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6420020" lon="-5.2394360">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:31Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>50</gpxtpx:watts>
      <gpxtpx:cad>76</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6419490" lon="-5.2394410">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:32Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>46</gpxtpx:watts>
      <gpxtpx:cad>73</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6419000" lon="-5.2394460">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:33Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>44</gpxtpx:watts>
      <gpxtpx:cad>70</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6418520" lon="-5.2394530">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:34Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>36</gpxtpx:watts>
      <gpxtpx:cad>61</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6418040" lon="-5.2394620">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:35Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>27</gpxtpx:watts>
      <gpxtpx:cad>52</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6417500" lon="-5.2394750">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:36Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>23</gpxtpx:watts>
      <gpxtpx:cad>48</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6417020" lon="-5.2394910">
    <ele>53.8</ele>
    <time>2024-09-12T12:28:37Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>18</gpxtpx:watts>
      <gpxtpx:cad>42</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6416540" lon="-5.2395110">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:38Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>16</gpxtpx:watts>
      <gpxtpx:cad>39</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6416050" lon="-5.2395310">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:39Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>13</gpxtpx:watts>
      <gpxtpx:cad>28</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6415570" lon="-5.2395520">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:40Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>9</gpxtpx:watts>
      <gpxtpx:cad>24</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6415090" lon="-5.2395740">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:41Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>9</gpxtpx:watts>
      <gpxtpx:cad>17</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6414710" lon="-5.2395950">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:42Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>2</gpxtpx:watts>
      <gpxtpx:cad>14</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6414340" lon="-5.2396120">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:43Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>14</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413960" lon="-5.2396270">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:44Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413690" lon="-5.2396390">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:45Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413530" lon="-5.2396470">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:46Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413370" lon="-5.2396530">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:47Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413260" lon="-5.2396570">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:48Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413260" lon="-5.2396590">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:49Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413210" lon="-5.2396590">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:50Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413210" lon="-5.2396590">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:51Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
   <trkpt lat="55.6413210" lon="-5.2396590">
    <ele>53.6</ele>
    <time>2024-09-12T12:28:52Z</time>
    <extensions>
     <gpxtpx:TrackPointExtension>
      <gpxtpx:watts>0</gpxtpx:watts>
      <gpxtpx:cad>0</gpxtpx:cad>
     </gpxtpx:TrackPointExtension>
    </extensions>
   </trkpt>
  </trkseg>
 </trk>
</gpx>
'''
    gpx_file = TMP_ROOT_FOLDER + 'sample.gpx'
    with open(gpx_file, 'w') as file:
        file.write(gpx_content)

    return gpx_file

def test_move_watts_to_power(gpx_file):
    # Define output path
    output_file = TMP_ROOT_FOLDER + 'modified_sample.gpx'
    
    # Call the function to test
    move_watts_to_power(gpx_file, output_file)
    
    # Check if the output file is created
    assert output_file.exists()
    
    # Parse the modified GPX file
    tree = ET.parse(output_file)
    root = tree.getroot()

    # Check if the <power> element is added and has the correct value
    power_element = root.find('power')
    assert power_element is not None