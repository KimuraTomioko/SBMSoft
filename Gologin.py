from gologin import GoLogin


gl = GoLogin({
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWE4MWEyODc3ZWYzOGIyMGFkNTQ2NGEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWFlMGI0NGQ4OTUzYWQ4MmU0NGUyM2EifQ.dr4Y6SGw6TnpsLMCnl4yTgvmDszSjUwViVKMJsX5wYg",
	})

profile_id = gl.create({
    "name": '9384293264',
    "os": 'mac',
    "navigator": {
        "language": 'en-US',
        "userAgent": 'random', # Your userAgent (if you don't want to change, leave it at 'random')
        "resolution": '1024x768', # Your resolution (if you want a random resolution - set it to 'random')
        "platform": 'mac',
    },
    'proxyEnabled': True, # Specify 'false' if not using proxy
    'proxy': {
        'mode': 'gologin',
        'autoProxyRegion': 'us' 
        # 'host': '',
        # 'port': '',
        # 'username': '',
        # 'password': '',
    },
    "webRTC": {
        "mode": "alerted",
        "enabled": True,
    },
});



