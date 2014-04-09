''' 
NOTE1: Close all SportsReview applications before editing as your changes may be lost.
NOTE2: File is regenerated upon changing a setting within GUI.  Only this DocString will be kept.

Timing:
-- (past) -- time -- (present) -->
----KKKKKKKKKKDDDDDDDDDDEEEEE
                       /\ captured frame
             /\ on-screen frame
K = keepalive
D = delay
E = extend

Settings:
- delay:     float, seconds between capturing a frame to displaying it when in playback mode.
- keepalive: float, seconds to keep frames for after they are displayed (i.e. used for backup in paused mode)
- extend:    float, seconds to keep recording frames for when pausing
- keybinding: dict, the key bindings for various functions.  Acceptable values from 'QtCore.Qt' package where name starts with 'Key_'.
    - quit
    - play
    - incdelay
    - decdelay
    - fullscreen
    - edit
    - record
    - help
- recorddirectory: str, the output directory for recorded captures.

'''
settings = {
	'delay': 1.0,
	'keepalive': 2.0,
	'extend': 1.0,
	'recorddirectory': '/tmp',
	'keybinding': {
		'quit': [
			'Escape',
			'Q',
		],
		'play': [
			'F7',
			'Space',
		],
		'decdelay': [
			'Less',
			'Minus',
			'Comma',
		],
		'fullscreen': [
			'F11',
		],
		'edit': [
			'F2',
		],
		'incdelay': [
			'Greater',
			'Plus',
			'Equal',
			'Period',
		],
		'help': [
			'F1',
		],
		'record': [
			'F12',
		],
	},
	'selectedlayout': 0,
	'layouts': [
		{
			'name': 'default',
			'captureframe': [
				('UsbCamCaptureCV', (0,)),
			],
            'processframe': [
                             ('FrameBuffer', ())
                             ],
		},
		{
			'name': 'cam2',
			'captureframe': [
				('UsbCamCaptureCV', (1,)),
			],
            'processframe': [
                             ('FrameBuffer', ())
                             ],
		},
	],
}
__order__= ['delay', 'keepalive', 'extend', 'recorddirectory', 'keybinding', 'selectedlayout', 'layouts']
