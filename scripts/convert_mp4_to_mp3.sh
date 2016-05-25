for i in *.m4a; do avconv -i "$i" "${i/.m4a/.mp3}" -acodec libmp3lame -ab 320; done
