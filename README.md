## Beskrivelse
Plugin for bruk på data på SOSI-format.<br>
Funksjoner vil bli lista under "SOSI" i funksjonslista man får opp i f.eks. Field Calculator.<br>
Foreløpig er det bare en funksjon (rotation_from_vector), men flere kan komme. Kom gjerne med innspill.<br>
<img src="https://github.com/9ls1/SOSIexpression/assets/10632163/6fee761e-9e4a-4ab8-b9fb-ccd077a55d39" alt="alt text" title="Funksjonsliste med SOSI" width="700"/>

Funksjonen ```rotation_from_vector("vectorfiled")``` omgjør egenskapsverdien i egenskapen vectorfield til rotasjonsvinkel i grader.<br>
Input-verdien forutsettes å være et koordinatpar (x y) fra enhetssirkelen (tekststreng med x- og y-verdi adskilt med et mellomrom).<br>
Se kapittel 14.1.3 og eksempel i 14.1.4 i [Realisering i SOSI-format versjon 5.0](https://standarder.geonorge.no/sosi/del-1-generell-del/realisering-i-sosi-format/5.0/realisering-i-sosi-format-50-sosi-generell-del.pdf). 

**Eksempel**<br>
Egenskapstabellen innholder egenskapen "symbolretning" på formen "x y".<br>
Da kan ny egenskap rot_degrees bergenes med ```rotate_from_vector( "symbolretning")```:<br>
<img src="https://github.com/9ls1/SOSIexpression/assets/10632163/f97d2e91-e506-49cf-b613-2b443a373d92" alt="alt text" title="Beregna rotasjonsvinkler i grader" width="325"/>

## Description
Plugin for use on data in SOSI format.<br>
Functions will be listed under "SOSI" in the function list you get in e.g. Field Calculator.<br>
Currently there is only one function (rotation_from_vector), but more may come. Feel free to suggest new features.

The function ```rotation_from_vector("vectorfiled")``` converts the attribute value in the vectorfield attribute to a rotation angle in degrees.<br>
The input value is assumed to be a coordinate pair (x y) from the unit circle (text string with x and y value separated by a space).<br>
See the image in chapter 14.1.3 in [Realisering i SOSI-format versjon 5.0](https://standarder.geonorge.no/sosi/del-1-generell-del/realisering-i-sosi-format/5.0/realisering-i-sosi-format-50-sosi-generell-del.pdf). 
