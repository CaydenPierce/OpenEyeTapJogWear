# OpenEyeTapJogWear


Jog function for the OpenEyeTap. Closely tracks location data.

## GPS Setup

The app uses GPS from an Android phone. This means that no new hardware need be added to the OpenEyeTap. Set up by:

Turn on Bluetooth on pi, make discoverable, trust your phone, then:

Run "Share GPS" app on your Anroid phone.:

http://www.jillybunch.com/sharegps/

And pair your phone to your pi. Make your device visible in the "Share GPS" app.

I wrote a lightweight bluetooth server to communicate with your phone, so your phone will now stream NMEA data to the OpenEyeTap.
