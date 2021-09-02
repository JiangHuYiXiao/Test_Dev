;ControlFocus ( "title", "text", controlID )

ControlFocus('打开','','Edit1')

;WinWait ( "title" [, "text" [, timeout = 0]] )
WinWait('[class:32770]','',10)

;Set the file name text on the edit field
ControlSetText('打开','','Edit1','F:\Python-Selenium\README.md')

;click on the open button
ControlClick('打开','','Button1')
