library verilog;
use verilog.vl_types.all;
entity Prac5 is
    port(
        Y               : out    vl_logic;
        D7              : in     vl_logic;
        D6              : in     vl_logic;
        D5              : in     vl_logic;
        D4              : in     vl_logic;
        D3              : in     vl_logic;
        D2              : in     vl_logic;
        D1              : in     vl_logic;
        D0              : in     vl_logic;
        A               : in     vl_logic_vector(2 downto 0)
    );
end Prac5;
