echo 'Sorted by dictionary size, time.'
printf '%-13s | %-13s | %-13s | %-13s | %-13s | %-13s\n' 'dict. (chars)' 'text (chars)' 'matches' 'time (ms)' 'log2(time)' 'time/char'
sort -t , -n -k2,2 -k6,6 $1 | awk -F',' '{printf "%13d | %13d | %13d | %13.5f | %13.5f | %13.5f\n",$2,$4,$5,$6,$7,$8}'

echo 'Sorted by text size, time.'
printf '%-13s | %-13s | %-13s | %-13s | %-13s | %-13s\n' 'text (chars)' 'dict. (chars)' 'matches' 'time (ms)' 'log2(time)' 'time/char'
sort -t , -n -k4,4 -k6,6 $1 | awk -F',' '{printf "%13d | %13d | %13d | %13.5f | %13.5f | %13.5f\n",$4,$2,$5,$6,$7,$8}'
