echo 'Run chimera-service'
setsid chimera-serve >/dev/null 2>&1 < /dev/null &

rm report.txt
touch report.txt

echo 'Perform test'
for i in `seq 1 5`;
do
    echo "Start test $i"
    chimera test-chimera.yaml >> report.txt
    echo "End test $i"
done

echo 'Show the result'
cat report.txt

python diagram.py

