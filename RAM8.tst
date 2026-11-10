load RAM8.hdl,
output-file RAM8.out,
compare-to RAM8.cmp,
output-list address%D3.1.3 out%D1.5.1;

set load 1,
set in 1822,
set address 5,
tick,
tock;

set in 3282,
set address 0,
tick,
tock;

set in 4983,
set address 3,
tick,
tock;

set load 0,
set address 0,
eval,
output;

set address 1,
eval,
output;

set address 2,
eval,
output;

set address 3,
eval,
output;

set address 4,
eval,
output;

set address 5,
eval,
output;

set address 6,
eval,
output;

set address 7,
eval,
output;

set address 3,
set in 4575,
set load 0,
tick,
tock,
eval,
output;