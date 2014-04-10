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
	'delay': 1.5,
	'keepalive': 2.0,
	'extend': 1.0,
	'recorddirectory': '/tmp',
	'keybinding': {
		'Space': [
			('core', 'play'),
		],
		'Equal': [
			('core', 'incdelay'),
			('core', 'incframe'),
		],
		'Q': [
			('core', 'quit'),
		],
		'Plus': [
			('core', 'incdelay'),
			('core', 'incframe'),
		],
		'F12': [
			('processgroup', 'RecordStillCV', ),
		],
		'F11': [
			('core', 'fullscreen'),
		],
		'Minus': [
			('core', 'decdelay'),
			('core', 'decframe'),
		],
		'F1': [
			('core', 'help'),
		],
		'F2': [
			('core', 'edit'),
		],
		'Greater': [
			('core', 'incdelay'),
			('core', 'incframe'),
		],
		'Less': [
			('core', 'decdelay'),
			('core', 'decframe'),
		],
		'F7': [
			('core', 'play'),
		],
		'Period': [
			('core', 'incdelay'),
			('core', 'incframe'),
		],
		'Comma': [
			('core', 'decdelay'),
			('core', 'decframe'),
		],
		'Escape': [
			('core', 'quit'),
		],
	},
	'selectedlayout': 0,
	'layouts': [
		{
			'name': 'default',
			'processframe': [
				('FrameExtend', ()),
				('FrameDelay', ()),
				('FrameStore', ()),
			],
			'captureframe': [
				('UsbCamCaptureCV', (0,)),
			],
		},
		{
			'name': 'cam2',
			'processframe': [
				('FrameExtend', ()),
				('FrameDelay', ()),
				('FrameStore', ()),
			],
			'captureframe': [
				('UsbCamCaptureCV', (1,)),
			],
		},
	],
}
__order__= ['delay', 'keepalive', 'extend', 'recorddirectory', 'keybinding', 'selectedlayout', 'layouts']
