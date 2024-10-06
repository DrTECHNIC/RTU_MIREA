onerror {exit -code 1}
vlib work
vlog -work work Prac1.vo
vlog -work work Waveform.vwf.vt
vsim -novopt -c -t 1ps -L cycloneiv_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.Prac1_vlg_vec_tst -voptargs="+acc"
vcd file -direction Prac1.msim.vcd
vcd add -internal Prac1_vlg_vec_tst/*
vcd add -internal Prac1_vlg_vec_tst/i1/*
run -all
quit -f
