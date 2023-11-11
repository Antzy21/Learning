title Lux main vs simple
echo main vs simple

cd ../../users/antho/documents

cd replays
del *.json
cd ..

cd errorlogs
deltree * /y
cd ..   

cd mine
tar -cvzf lux1.tar.gz *.py lux\*
cd ..

start lux-ai-2021 mine/main.py old/main.py