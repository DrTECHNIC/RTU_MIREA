library verilog;
use verilog.vl_types.all;
entity Prac7_vlg_sample_tst is
    port(
        a               : in     vl_logic;
        b               : in     vl_logic;
        clock           : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end Prac7_vlg_sample_tst;
