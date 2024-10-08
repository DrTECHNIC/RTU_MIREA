onerror {exit -code 1}
vlib work
vlog -work work Prac5.vo
vlog -work work Waveform.vwf.vt
vsim -novopt -c -t 1ps -L cycloneiv_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.Prac5_vlg_vec_tst -voptargs="+acc"
vcd file -direction Prac5.msim.vcd
vcd add -internal Prac5_vlg_vec_tst/*
vcd add -internal Prac5_vlg_vec_tst/i1/*
run -all
quit -f
