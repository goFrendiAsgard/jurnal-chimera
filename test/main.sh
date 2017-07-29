CONFIG_FILE="$1"
REPORT_FILE="$2"
TEST_FILE="$3"
TEST_COUNT=10

# Change directory and run server
echo 'Change Directory'
cd node_modules/chimera-framework
echo 'Run chimera-service'

PORT=3010 chimera-serve &

# Delete old report file and create a new one
echo 'Create report file'
rm "$REPORT_FILE"
touch "$REPORT_FILE"

# Do the test
echo 'Perform test'
for i in `seq 1 $TEST_COUNT`;
do
    echo "Start test $i"
    chimera tests/chain-distributed.yaml 4 5 http://localhost:3010 2>> "$REPORT_FILE"
    echo "End test $i"
done

# kill the server
pkill node

echo 'Show the result'
cat "$REPORT_FILE"

python ../../diagram.py "$CONFIG_FILE" "$REPORT_FILE"
cd ../../
