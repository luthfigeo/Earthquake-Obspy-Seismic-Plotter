import obspy
from obspy.clients.fdsn import Client
c = 'IRIS'
client = Client(c)
from obspy import UTCDateTime

t = UTCDateTime('2021-01-14T18:28:00')
[sbef, saft] = [0,2400]
st = client.get_waveforms('IU','DAV','10','BHZ', t-sbef, t+saft, attach_response = True)
#st = st.select(component='Z')
st.plot(linewidth=0.75, equal_scale = False)


st = client.get_waveforms('IU','MBWA','10','BHZ', t-sbef, t+saft, attach_response = True)
#st = st.select(component='Z')
st.plot(linewidth=0.75, equal_scale = False)

st = client.get_waveforms('IU','PMG','10','BHZ', t-sbef, t+saft, attach_response = True)
#st = st.select(component='Z')
st.plot(linewidth=0.75, equal_scale = False)