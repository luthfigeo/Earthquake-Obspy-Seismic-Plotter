import obspy
from obspy.clients.fdsn import Client
c = 'IRIS'
client = Client(c)
from obspy import UTCDateTime

t = UTCDateTime('2021-01-14T18:28:00')
[sbef, saft] = [0,2400]
st0 = client.get_waveforms('IU','DAV','10','BHZ', t-sbef, t+saft, attach_response = True)
st0.remove_response(output='VEL')
st0.plot(linewidth=0.5, equal_scale = False)

st1 = client.get_waveforms('IU','MBWA','10','BHZ', t-sbef, t+saft, attach_response = True)
st1.remove_response(output='VEL')
st1.plot(linewidth=0.5, equal_scale = False)

st2 = client.get_waveforms('IU','PMG','10','BHZ', t-sbef, t+saft, attach_response = True)
st2.remove_response(output='VEL')
st2.plot(linewidth=0.5, equal_scale = False)