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
		'Comma': [
			('core', 'decdelay'),
			('core', 'decframe'),
		],
		'Equal': [
			('core', 'incdelay'),
			('core', 'incframe'),
		],
		'Escape': [
			('core', 'quit'),
		],
		'F1': [
			('core', 'help'),
		],
		'F10': [
			('processgroup', 'AviWriterCV', 0),
		],
		'F11': [
			('core', 'fullscreen'),
		],
		'F12': [
			('processgroup', 'JpegStillArrayWriter'),
		],
		'F2': [
			('core', 'edit'),
		],
		'F7': [
			('core', 'play'),
		],
		'Greater': [
			('core', 'incdelay'),
			('core', 'incframe'),
		],
		'Less': [
			('core', 'decdelay'),
			('core', 'decframe'),
		],
		'Minus': [
			('core', 'decdelay'),
			('core', 'decframe'),
		],
		'Period': [
			('core', 'incdelay'),
			('core', 'incframe'),
		],
		'Plus': [
			('core', 'incdelay'),
			('core', 'incframe'),
		],
		'Q': [
			('core', 'quit'),
		],
		'Space': [
			('core', 'play'),
		],
	},
	'selectedlayout': 0,
	'layouts': [
		{
			'captureframe': [
				('UsbCamCaptureCV', (0,)),
			],
			'name': 'default',
			'processframe': [
				('FrameExtend', ()),
				('FrameDelay', ()),
				('FrameStore', ()),
			],
			'screen': [
				(0, 0.0, 0.0, 0.9, 1.0),
			],
		},
		{
			'captureframe': [
				('UsbCamCaptureCV', (1,)),
			],
			'name': 'cam2',
			'processframe': [
				('FrameExtend', ()),
				('FrameDelay', ()),
				('FrameStore', ()),
			],
			'screen': [
				(0, 0.0, 0.0, 1.0, 1.0),
			],
		},
		{
			'captureframe': [
				('UsbCamCaptureCV', (0,)),
				('UsbCamCaptureCV', (1,)),
			],
			'name': 'cam2',
			'processframe': [
				('FrameExtend', ()),
				('FrameDelay', ()),
				('FrameStore', ()),
			],
			'screen': [
				(0, 0.0, 0.0, 1.0, 0.7),
				(1, 0.7, 0.6, 1.0, 1.0),
			],
		},
	],
	'aftertouchesui': {
		'geometry': (1, 39, 746, 715),
		'mode': 'normal',
		'savegeometry': True,
		'savemode': True,
	},
	'delayanalysisui': {
		'geometry': (77, 54, 960, 768),
		'mode': 'normal',
		'savegeometry': True,
		'savemode': True,
	},
}
__order__= ['delay', 'keepalive', 'extend', 'recorddirectory', 'keybinding', 'selectedlayout', 'layouts', 'aftertouchesui', 'delayanalysisui']
