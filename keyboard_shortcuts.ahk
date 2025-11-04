F1::copy()
F2::copyEntryToAnki()

copyEntryToAnki(){

	short_wait 	:= 50
	long_wait 	:= 300

	MouseClick "left", 1140, 57 ; Copy word
	Sleep short_wait
	
	MouseClick "left", 620, 1200 ; Choose Wort field
	Sleep short_wait
	
	replacePaste() ; Paste word
	Sleep short_wait

	MouseClick "left", 1140, -985 ; Copy grammar
	pasteIntoAnki(short_wait)

	MouseClick "left", 1140, -925 ; Copy meaning
	pasteIntoAnki(short_wait)

	MouseClick "left", 1140, -640 ; Copy examples
	switchAndNext(short_wait)
	Send "^V"
	Sleep long_wait

	MouseClick "left", 1140, -355 ; Copy thesaurus
	pasteIntoAnki(short_wait)

	MouseClick "left", 1140, -77 ; Copy tags
	
	switchAndNext(short_wait)
	Send "^{Backspace 6}"
	Sleep short_wait
	Send "^V"
	Sleep short_wait
	Send "{Enter}"
	Return
}

replacePaste(){
	Send ("^a")
	Send ("^v")
	Return
}

pasteIntoAnki(short_wait){
	switchAndNext(short_wait)
	Send "^V"
	Sleep short_wait
	Return
}

switchAndNext(short_wait){
	Sleep short_wait
	Send ("!{Tab}")
	Sleep short_wait
	Send "{Tab}"
	Sleep short_wait
	Return
}

highligh(){
	Send("^i")
	Send("{F7}")
	Return
}