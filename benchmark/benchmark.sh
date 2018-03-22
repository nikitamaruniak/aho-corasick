if ! [ -d 'testdata' ]
then
    tar -jxvf testdata.tbz2
fi

rm -f benchmark_results.txt
touch benchmark_results.txt
for text in testdata/test_text*
do
    for dict in testdata/test_dict*
    do
        python benchmark.py "$dict" "$text" | tee -a benchmark_results.txt
    done
done

./format_results.sh benchmark_results.txt
