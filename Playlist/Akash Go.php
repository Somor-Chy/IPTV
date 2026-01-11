<?php

$url = "https://akashgo.noobmaster.xyz/?api=iptv_m3u";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   "User-Agent: okhttp/4.12.0",
   "X-Requested-With: com.blaze.sportzfy",
   "Accept-Encoding: gzip",
   "Connection: Keep-Alive",
   "Referer: https://akashgo.noobmaster.xyz/",
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

$resp = curl_exec($curl);
curl_close($curl);
var_dump($resp);

?>