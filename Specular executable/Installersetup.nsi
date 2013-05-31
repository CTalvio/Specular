	!include "MUI.nsh"
	
;--------------------------------

	Name "Specular"

	OutFile "SPInstall a0.4.exe"

	InstallDir "C:\Games\Specular"
	
;--------------------------------

	!define MUI_ICON "Install.ico"
	!define MUI_WELCOMEFINISHPAGE_BITMAP "Specular.bmp" 
	!define MUI_HEADERIMAGE 
	!define MUI_HEADERIMAGE_RIGHT
	!define MUI_HEADERIMAGE_BITMAP "Header.bmp"
	
;--------------------------------

	!define MUI_WELCOMEPAGE_TITLE "Specular alpha v0.4"

;--------------------------------
	
	!insertmacro MUI_PAGE_WELCOME
	!insertmacro MUI_PAGE_DIRECTORY
	!insertmacro MUI_PAGE_INSTFILES
	!insertmacro MUI_PAGE_FINISH
	
;--------------------------------

	!insertmacro MUI_LANGUAGE "English"
	
;--------------------------------

Section "Installing time!"

	SetOutPath $INSTDIR

	File /a Specular.exe
	File w9xpopen.exe
	File jpeg.dll
	File libfreetype-6.dll
	File libogg-0.dll
	File libpng12-0.dll
	File libvorbis-0.dll
	File libvorbisfile-3.dll
	File portmidi.dll
	File python27.dll
	File smpeg.dll
	File zlib1.dll
	File SDL.dll
	File SDL_image.dll
	File SDL_mixer.dll
	File SDL_ttf.dll
	File /r Audio
	File /r Enemy_1
	File /r Enemy_2
	File /r Font
	File /r Player
	File /r Textures
	
	CreateShortCut "$SMPROGRAMS\Specular.lnk" "$INSTDIR\Specular.exe" "" "$INSTDIR\Textures\Icon.ico"


SectionEnd


