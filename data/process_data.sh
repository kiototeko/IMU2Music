#! /bin/bash

array=($(find . -type d | grep -oE "[0-9][0-9]_.*"))

FPS=25

for i in "${array[@]}"
do

        echo "DIRECTORY: ${i}"
        
        TOTAL_LEN=$(sox ${i}/00_audio_pickup.wav -n stat 2>&1 | sed -n 's#^Length (seconds):[^0-9]*\([0-9.]*\)$#\1#p')
	INIT_SILENCE=$(sox ${i}/00_audio_pickup.wav -n silence -l 1 0.1 1% stat 2>&1 | sed -n 's#^Length (seconds):[^0-9]*\([0-9.]*\)$#\1#p')
	END_SILENCE=$(sox ${i}/00_audio_pickup.wav -n  reverse silence -l 1 0.1 1% reverse stat 2>&1 | sed -n 's#^Length (seconds):[^0-9]*\([0-9.]*\)$#\1#p')
	INIT_SILENCE=$(python -c "from math import ceil; print(ceil($TOTAL_LEN - $INIT_SILENCE))")
	END_SILENCE=$(python -c "from math import floor; print(floor($END_SILENCE))")
	DURATION=$(($END_SILENCE - $INIT_SILENCE))
	
	if [ $DURATION -lt 1 ]
	then
                echo "No audio"
                continue
	fi
	
	IMU_LEN=$(tail -n 1 ${i}/00_myo1_gyro__x.csv | grep -o , | wc -l)
	IMU_LEN=$(python -c "from math import floor; print(floor($IMU_LEN/$FPS))")
        echo "$INIT_SILENCE, $DURATION, $END_SILENCE, $TOTAL_LEN, $IMU_LEN"
	if [ $(($INIT_SILENCE + $DURATION)) -gt $IMU_LEN ]
	then
                DURATION=$(($IMU_LEN - $INIT_SILENCE))
        fi
	
	sox ${i}/00_audio_pickup.wav samples/audio/${i}.wav trim $INIT_SILENCE $DURATION
	
	sensors=("acceleration" "gyro" "Rotation")
	axis=("x" "y" "z")
	
	
	
	for j in {1..2}
	do
                for s in "${sensors[@]}"
                do
                        for a in "${axis[@]}"
                        do
                                LINE=$(tail -n 1 ${i}/00_myo${j}_${s}__${a}.csv)
                                readarray -d "," -t samples<<<"$LINE"
                                START=$(($INIT_SILENCE*$FPS))
                                NEW_LINE=""
                                for (( v=$START; v<$(($DURATION*$FPS + $START)); v++ ))
                                do
                                                NEW_LINE+="${samples[$v]},"
                                done
                                
                                head -n 1 ${i}/00_myo${j}_${s}__${a}.csv > samples/imu/${i}_${s}_${a}${j}.csv
                                echo $NEW_LINE >> samples/imu/${i}_${s}_${a}${j}.csv
                        done
                done
        done
		

	#cp ${i}/00_audio_pickup.wav samples/audio/${i}.wav
	
	#./AnthemScore-x86_64.AppImage ${i}/00_audio_pickup.wav -m samples/midi/${i}.midi
	../WaoN/waon -i samples/audio/${i}.wav -o samples/midi/${i}.midi -t 108 -b 21

	
done
