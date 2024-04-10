<h1>SENSE eeeZeee</h1>

<h3>Raspbian Bullseye. Python 3. Minimal demo.</h3> 

<h4>Sensor data acquisition. Flask API exposed at your_IP_address_here:5000/getData</h4> 

<h4>CO2. Temperature. Humidity. Air Pressure.</h4>

<h3>Sensors:</h3>

- BME280 - I2C

- Senseair K30 - serial

- RTC DS3231 - I2C

- LCD1602 - I2C

<h3>Commands:</h3>

start data collection: 
* <b>python data.py</b>

start Flask: 
* <b>flask --app dataAPI run --host=0.0.0.0 --debug</b>

wipe out/ initialize DB: 
* <b>flask --app dataAPI init-db</b>


All files are released under a [MIT license](https://en.wikipedia.org/wiki/MIT_License)
  
