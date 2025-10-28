F2::highligh()
F1::copy()

highligh(){
Send("^i")
Send("{F7}")
Return
}

copy(){
MouseClick "left", 1140, 57 ; Copy word
Sleep 100
MouseClick "left", 620, 1200 ; Choose Wort field
Sleep 700
Send ("^a") ; Paste
Send "^V" ; Paste
Sleep 100
MouseClick "left", 1140, -985 ; Copy grammar
paste()
MouseClick "left", 1140, -925 ; Copy meaning
paste()
MouseClick "left", 1140, -640 ; Copy examples
paste()
MouseClick "left", 1140, -355 ; Copy thesaurus
paste()
MouseClick "left", 1140, -77 ; Copy tags
Sleep 700
MouseClick "left", 620, 1060
Sleep 100
Send "{Tab}"
Sleep 100
Send "^{Backspace 6}"
Sleep 100
Send "^V"
Sleep 100
Send "{Enter}"
}

paste(){
Sleep 700
MouseClick "left", 620, 1060
Sleep 100
Send "{Tab}"
Sleep 100
Send "^V"
Sleep 100
}