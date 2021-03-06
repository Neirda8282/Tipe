import sys
import time 
from PhidgetHelperFunctions import *
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

# ph.setDataInterval(1000) # intervalle de temps entre les données
# ph.setVoltageRatiochangeTrigger(0.0) # trigger de detectin seuil de detection   
def onAttachHandler(self):
    
    ph = self

    """
    * Set the DataInterval inside of the attach handler to initialize the device with this value.
    * DataInterval defines the minimum time between VoltageRatioChange events.
    * DataInterval can be set to any value from MinDataInterval to MaxDataInterval.
    """
    print("\tSetting DataInterval to 1000ms")
    try:
        ph.setDataInterval(1000)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Setting DataInterval: \n\t")
        DisplayError(e)
        return

    """
    * Set the VoltageRatioChangeTrigger inside of the attach handler to initialize the device with this value.
    * VoltageRatioChangeTrigger will affect the frequency of VoltageRatioChange events, by limiting them to only occur when
    * the voltage ratio changes by at least the value set.
    """
    print("\tSetting VoltageRatio ChangeTrigger to 0.0")
    try:
        ph.setVoltageRatioChangeTrigger(0.0)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Set VoltageRatioChangeTrigger: \n\t")
        DisplayError(e)
        return

    """
    * Set the SensorType inside of the attach handler to initialize the device with this value.
    * SensorType will apply the appropriate calculations to the voltage ratio reported by the device
    * to convert it to the sensor's units.
    * SensorType can only be set for Sensor Port voltage ratio inputs (VINT Ports and Analog Input Ports)
    """
    if(ph.getChannelSubclass() == ChannelSubclass.PHIDCHSUBCLASS_VOLTAGERATIOINPUT_SENSOR_PORT):
        print("\tSetting VoltageRatio SensorType")
        try:
            ph.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_VOLTAGERATIO)
        except PhidgetException as e:
            sys.stderr.write("Runtime Error -> Set SensorType: \n\t")
            DisplayError(e)
            return
        
    try:
        serialNumber = ph.getDeviceSerialNumber()
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Get DeviceSerialNumber: \n\t")
        DisplayError(e)
        return

    try:
        channel = ph.getChannel()
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Get Channel: \n\t")
        DisplayError(e)
        return

    # Check if this is a VINT device
    try:
        hub = ph.getHub()
    except PhidgetException as e:
        if(e.code == ErrorCode.EPHIDGET_WRONGDEVICE):
            print("\nAttach Event:\n\t-> Serial Number: " + str(serialNumber) +
                    "\n\t-> Channel " + str(channel) + "\n")
        return
    try:
        hubPort = ph.getHubPort()
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Get HubPort: \n\t")
        DisplayError(e)
        return

    print("\nAttach Event:\n\t-> Serial Number: " + str(serialNumber) +
          "\n\t-> Hub Port: " + str(hubPort) + "\n\t-> Channel " + str(channel) + "\n")    
    return

"""
* Displays info about the detached phidget channel.
* Fired when a Phidget channel with onDetachHandler registered detaches
*
* @param self The Phidget channel that fired the attach event
"""
def onDetachHandler(self):

    ph = self

    try:
        serialNumber = ph.getDeviceSerialNumber()
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Get DeviceSerialNumber: \n\t")
        DisplayError(e)
        return

    try:
        channel = ph.getChannel()
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Get Channel: \n\t")
        DisplayError(e)
        return

     # Check if this is a VINT device
    try:
        hub = ph.getHub()
    except PhidgetException as e:
        if(e.code == ErrorCode.EPHIDGET_WRONGDEVICE):
            print("\nDetach Event:\n\t-> Serial Number: " + str(serialNumber) +
                    "\n\t-> Channel " + str(channel) + "\n")
        return

    try:
        hubPort = ph.getHubPort()
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Get HubPort: \n\t")
        DisplayError(e)
        return

    print("\nDetach Event:\n\t-> Serial Number: " + str(serialNumber) +
          "\n\t-> Hub Port: " + str(hubPort) + "\n\t-> Channel " + str(channel) + "\n")
    return

"""
* Writes phidget error info to stderr.
* Fired when a Phidget channel with onErrorHandler registered encounters an error in the library
*
* @param self The Phidget channel that fired the attach event
* @param errorCode the code associated with the error of enum type ph.ErrorEventCode
* @param errorString string containing the description of the error fired
"""
def onErrorHandler(self, errorCode, errorString):

    sys.stderr.write("[Phidget Error Event] -> " + errorString + " (" + str(errorCode) + ")\n")

"""
* Sets the event handlers for Phidget Attach, Phidget Detach, Phidget Error events
*
* @param ph The Phidget channel to add event handlers to
* @return if the operation succeeds
* @raise PhidgetException if it fails
"""
def SetAttachDetachError_Handlers(ph):
    print("\n--------------------------------------")
    print("\nSetting OnAttachHandler...")
    try:
        ph.setOnAttachHandler(onAttachHandler)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Set Attach Handler: \n\t")
        DisplayError(e)
        raise

    print("Setting OnDetachHandler...")
    try:
        ph.setOnDetachHandler(onDetachHandler)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Set Detach Handler: \n\t")
        DisplayError(e)
        raise

    print("Setting OnErrorHandler...")
    try:
        ph.setOnErrorHandler(onErrorHandler)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Set Error Handler: \n\t")
        DisplayError(e)
        raise

    return

"""
* Outputs the VoltageRatioInput's most recently reported voltage ratio.
* Fired when a VoltageRatioInput channel with onVoltageRatioChangeHandler registered meets DataInterval and ChangeTrigger criteria
*
* @param self The VoltageRatioInput channel that fired the VoltageRatioChange event
* @param ratio The reported voltage ratio from the VoltageRatioInput channel
"""
def onVoltageRatioChangeHandler(self, ratio):

    print("[VoltageRatio Event] -> VoltageRatio: " + str(ratio))

"""
* Outputs the VoltageRatioInput's most recently reported sensor value.
* Fired when a VoltageRatioInput channel with onSensorChangeHandler registered meets DataInterval and ChangeTrigger criteria
*
* @param self The VoltageRatioInput channel that fired the SensorChange event
* @param sensorValue The reported sensor value from the VoltageRatioInput channel
"""
def onSensorChangeHandler(self, sensorValue, sensorUnit):

    print("[Sensor Event] -> Sensor Value: " + str(sensorValue) + sensorUnit.symbol)
    
"""
* Creates a new instance of a VoltageRatioInput channel.
*
* @param pvih Pointer to the PhidgetVoltageRatioInputHandle channel to create
* @return if the operation succeeds
* @raise PhidgetException if it fails
"""
def CreateVoltageRatioInput(pvih):

    print("Creating VoltageRatioInput Channel...")
    try:
        pvih.create()
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Creating VoltageRatioInput: \n\t")
        DisplayError(e)
        raise

    return

"""
* Sets the event handler for VoltageRatioInput's VoltageRatioChange event
*
* @param pvih The PhidgetVoltageRatioInputHandle channel to add the event to
* @param fptr The callback function to be called when a VoltageRatioChange event is fired
* @return if the operation succeeds
* @raise PhidgetException if it fails
"""
def SetVoltageRatioHandler(pvih, fptr):

    if (not (fptr is None)):
        print("\n--------------------\n"
            "\n  | VoltageRatio change events contain the most recent voltage ratio received from the device.\n"
            "  | The linked VoltageRatioChange function will run as an event at every DataInterval.\n"
            "  | These events will not occur until a change in voltage ratio >= to the set ChangeTrigger has occured.\n"
            "  | DataInterval and ChangeTrigger should initially be set in the device AttachHandler function.")
    
    print("")
    if (fptr is None):
        print("Clearing OnVoltageRatioChangeHandler...")
    else:
        print("Setting OnVoltageRatioChangeHandler...")

    print("\n--------------------")
    try:
        pvih.setOnVoltageRatioChangeHandler(fptr)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Setting VoltageRatioChangeHandler: \n\t")
        DisplayError(e)
        raise
    
    return

"""
* Sets the event handler for VoltageRatioInput's SensorChange event
*
* @param pvih The PhidgetVoltageRatioInputHandle channel to add the event to
* @param fptr The callback function to be called when a SensorChange event is fired
* @return if the operation succeeds
* @raise PhidgetException if it fails
"""
def SetSensorHandler(pvih, fptr):

    if (not (fptr is None)):
        print("\n--------------------\n"
            "\n  | Sensor change events contain the most recent sensor value received from the device.\n"
            "  | Sensor change events will occur instead of VoltageRatio change events if the SensorType is changed from the default."
            "  | The linked SensorChange function will run as an event at every DataInterval.\n"
            "  | These events will not occur until a change in sensor value >= to the set ChangeTrigger has occurred.\n"
            "  | DataInterval, ChangeTrigger and SensorType should initially be set in the device AttachHandler function.")
    
    print("")
    if (fptr is None):
        print("Clearing OnSensorChangeHandler...")
    else:
        print("Setting OnSensorChangeHandler...")

    print("\n--------------------")
    try:
        pvih.setOnSensorChangeHandler(fptr)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Setting SensorChangeHandler: \n\t")
        DisplayError(e)
        raise
    
    return
    print("\n--------------------------------------")
    print("\nSetting OnAttachHandler...")
    try:
        ph.setOnAttachHandler(onAttachHandler)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Set Attach Handler: \n\t")
        DisplayError(e)
        raise

    print("Setting OnDetachHandler...")
    try:
        ph.setOnDetachHandler(onDetachHandler)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Set Detach Handler: \n\t")
        DisplayError(e)
        raise

    print("Setting OnErrorHandler...")
    try:
        ph.setOnErrorHandler(onErrorHandler)
    except PhidgetException as e:
        sys.stderr.write("Runtime Error -> Set Error Handler: \n\t")
        DisplayError(e)
        raise

    return

 
 
ch=VoltageRatioInput()

 
ch.openWaitForAttachment(5000)
# ch.setDeviceSerialNumber(-1)
# ch.setChannel(2)
# # ch.setDataInterval(1000)
# # ch.setVoltageRatioChangeTrigger(0.0)


# SetAttachDetachError_Handlers(ch)
# SetVoltageRatioHandler(ch,onVoltageRatioChangeHandler)
# SetSensorHandler(ch,onSensorChangeHandler)
# OpenPhidgetChannel_waitForAttach(ch,5000)







state=ch.getVoltageRatio()
print(state)