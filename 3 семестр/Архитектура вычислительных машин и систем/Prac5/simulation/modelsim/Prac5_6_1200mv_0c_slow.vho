-- Copyright (C) 1991-2013 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, Altera MegaCore Function License 
-- Agreement, or other applicable license agreement, including, 
-- without limitation, that your use is for the sole purpose of 
-- programming logic devices manufactured by Altera and sold by 
-- Altera or its authorized distributors.  Please refer to the 
-- applicable agreement for further details.

-- VENDOR "Altera"
-- PROGRAM "Quartus II 64-Bit"
-- VERSION "Version 13.1.0 Build 162 10/23/2013 SJ Web Edition"

-- DATE "10/08/2024 10:41:33"

-- 
-- Device: Altera EP4CGX15BF14C6 Package FBGA169
-- 

-- 
-- This VHDL file should be used for ModelSim-Altera (VHDL) only
-- 

LIBRARY CYCLONEIV;
LIBRARY IEEE;
USE CYCLONEIV.CYCLONEIV_COMPONENTS.ALL;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY 	Prac5 IS
    PORT (
	Y : OUT std_logic;
	D7 : IN std_logic;
	D6 : IN std_logic;
	D5 : IN std_logic;
	D4 : IN std_logic;
	D3 : IN std_logic;
	D2 : IN std_logic;
	D1 : IN std_logic;
	D0 : IN std_logic;
	A : IN std_logic_vector(2 DOWNTO 0)
	);
END Prac5;

-- Design Ports Information
-- Y	=>  Location: PIN_A6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- D6	=>  Location: PIN_M6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- A[1]	=>  Location: PIN_N11,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- D5	=>  Location: PIN_N6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- A[0]	=>  Location: PIN_M4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- D4	=>  Location: PIN_N8,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- D7	=>  Location: PIN_L4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- D1	=>  Location: PIN_A8,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- D2	=>  Location: PIN_L7,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- D0	=>  Location: PIN_K9,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- D3	=>  Location: PIN_G13,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- A[2]	=>  Location: PIN_H13,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF Prac5 IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_Y : std_logic;
SIGNAL ww_D7 : std_logic;
SIGNAL ww_D6 : std_logic;
SIGNAL ww_D5 : std_logic;
SIGNAL ww_D4 : std_logic;
SIGNAL ww_D3 : std_logic;
SIGNAL ww_D2 : std_logic;
SIGNAL ww_D1 : std_logic;
SIGNAL ww_D0 : std_logic;
SIGNAL ww_A : std_logic_vector(2 DOWNTO 0);
SIGNAL \Y~output_o\ : std_logic;
SIGNAL \A[0]~input_o\ : std_logic;
SIGNAL \D3~input_o\ : std_logic;
SIGNAL \D1~input_o\ : std_logic;
SIGNAL \D0~input_o\ : std_logic;
SIGNAL \D2~input_o\ : std_logic;
SIGNAL \A[1]~input_o\ : std_logic;
SIGNAL \inst1|LPM_MUX_component|auto_generated|_~2_combout\ : std_logic;
SIGNAL \inst1|LPM_MUX_component|auto_generated|_~3_combout\ : std_logic;
SIGNAL \D6~input_o\ : std_logic;
SIGNAL \D7~input_o\ : std_logic;
SIGNAL \D5~input_o\ : std_logic;
SIGNAL \D4~input_o\ : std_logic;
SIGNAL \inst1|LPM_MUX_component|auto_generated|_~0_combout\ : std_logic;
SIGNAL \inst1|LPM_MUX_component|auto_generated|_~1_combout\ : std_logic;
SIGNAL \A[2]~input_o\ : std_logic;
SIGNAL \inst1|LPM_MUX_component|auto_generated|_~4_combout\ : std_logic;

BEGIN

Y <= ww_Y;
ww_D7 <= D7;
ww_D6 <= D6;
ww_D5 <= D5;
ww_D4 <= D4;
ww_D3 <= D3;
ww_D2 <= D2;
ww_D1 <= D1;
ww_D0 <= D0;
ww_A <= A;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;

-- Location: IOOBUF_X10_Y31_N2
\Y~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \inst1|LPM_MUX_component|auto_generated|_~4_combout\,
	devoe => ww_devoe,
	o => \Y~output_o\);

-- Location: IOIBUF_X8_Y0_N1
\A[0]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_A(0),
	o => \A[0]~input_o\);

-- Location: IOIBUF_X33_Y16_N22
\D3~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_D3,
	o => \D3~input_o\);

-- Location: IOIBUF_X12_Y31_N8
\D1~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_D1,
	o => \D1~input_o\);

-- Location: IOIBUF_X22_Y0_N1
\D0~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_D0,
	o => \D0~input_o\);

-- Location: IOIBUF_X14_Y0_N1
\D2~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_D2,
	o => \D2~input_o\);

-- Location: IOIBUF_X26_Y0_N1
\A[1]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_A(1),
	o => \A[1]~input_o\);

-- Location: LCCOMB_X18_Y2_N12
\inst1|LPM_MUX_component|auto_generated|_~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \inst1|LPM_MUX_component|auto_generated|_~2_combout\ = (\A[0]~input_o\ & (((\A[1]~input_o\)))) # (!\A[0]~input_o\ & ((\A[1]~input_o\ & ((\D2~input_o\))) # (!\A[1]~input_o\ & (\D0~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111101001000100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \A[0]~input_o\,
	datab => \D0~input_o\,
	datac => \D2~input_o\,
	datad => \A[1]~input_o\,
	combout => \inst1|LPM_MUX_component|auto_generated|_~2_combout\);

-- Location: LCCOMB_X18_Y2_N6
\inst1|LPM_MUX_component|auto_generated|_~3\ : cycloneiv_lcell_comb
-- Equation(s):
-- \inst1|LPM_MUX_component|auto_generated|_~3_combout\ = (\A[0]~input_o\ & ((\inst1|LPM_MUX_component|auto_generated|_~2_combout\ & (\D3~input_o\)) # (!\inst1|LPM_MUX_component|auto_generated|_~2_combout\ & ((\D1~input_o\))))) # (!\A[0]~input_o\ & 
-- (((\inst1|LPM_MUX_component|auto_generated|_~2_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1101110110100000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \A[0]~input_o\,
	datab => \D3~input_o\,
	datac => \D1~input_o\,
	datad => \inst1|LPM_MUX_component|auto_generated|_~2_combout\,
	combout => \inst1|LPM_MUX_component|auto_generated|_~3_combout\);

-- Location: IOIBUF_X12_Y0_N8
\D6~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_D6,
	o => \D6~input_o\);

-- Location: IOIBUF_X8_Y0_N8
\D7~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_D7,
	o => \D7~input_o\);

-- Location: IOIBUF_X12_Y0_N1
\D5~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_D5,
	o => \D5~input_o\);

-- Location: IOIBUF_X20_Y0_N8
\D4~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_D4,
	o => \D4~input_o\);

-- Location: LCCOMB_X18_Y2_N8
\inst1|LPM_MUX_component|auto_generated|_~0\ : cycloneiv_lcell_comb
-- Equation(s):
-- \inst1|LPM_MUX_component|auto_generated|_~0_combout\ = (\A[0]~input_o\ & ((\D5~input_o\) # ((\A[1]~input_o\)))) # (!\A[0]~input_o\ & (((\D4~input_o\ & !\A[1]~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1010101011011000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \A[0]~input_o\,
	datab => \D5~input_o\,
	datac => \D4~input_o\,
	datad => \A[1]~input_o\,
	combout => \inst1|LPM_MUX_component|auto_generated|_~0_combout\);

-- Location: LCCOMB_X18_Y2_N2
\inst1|LPM_MUX_component|auto_generated|_~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \inst1|LPM_MUX_component|auto_generated|_~1_combout\ = (\inst1|LPM_MUX_component|auto_generated|_~0_combout\ & (((\D7~input_o\) # (!\A[1]~input_o\)))) # (!\inst1|LPM_MUX_component|auto_generated|_~0_combout\ & (\D6~input_o\ & ((\A[1]~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1100101011110000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \D6~input_o\,
	datab => \D7~input_o\,
	datac => \inst1|LPM_MUX_component|auto_generated|_~0_combout\,
	datad => \A[1]~input_o\,
	combout => \inst1|LPM_MUX_component|auto_generated|_~1_combout\);

-- Location: IOIBUF_X33_Y16_N15
\A[2]~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_A(2),
	o => \A[2]~input_o\);

-- Location: LCCOMB_X18_Y2_N0
\inst1|LPM_MUX_component|auto_generated|_~4\ : cycloneiv_lcell_comb
-- Equation(s):
-- \inst1|LPM_MUX_component|auto_generated|_~4_combout\ = (\A[2]~input_o\ & ((\inst1|LPM_MUX_component|auto_generated|_~1_combout\))) # (!\A[2]~input_o\ & (\inst1|LPM_MUX_component|auto_generated|_~3_combout\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1100110010101010",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \inst1|LPM_MUX_component|auto_generated|_~3_combout\,
	datab => \inst1|LPM_MUX_component|auto_generated|_~1_combout\,
	datad => \A[2]~input_o\,
	combout => \inst1|LPM_MUX_component|auto_generated|_~4_combout\);

ww_Y <= \Y~output_o\;
END structure;


