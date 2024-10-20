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

-- DATE "10/20/2024 15:03:15"

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

ENTITY 	Prac7 IS
    PORT (
	a : IN std_logic;
	b : IN std_logic;
	clock : IN std_logic;
	q3 : OUT std_logic;
	q2 : OUT std_logic;
	q1 : OUT std_logic;
	q0 : OUT std_logic
	);
END Prac7;

-- Design Ports Information
-- clock	=>  Location: PIN_B6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- q3	=>  Location: PIN_N8,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- q2	=>  Location: PIN_M6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- q1	=>  Location: PIN_M4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- q0	=>  Location: PIN_L4,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- a	=>  Location: PIN_L5,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b	=>  Location: PIN_N4,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF Prac7 IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_a : std_logic;
SIGNAL ww_b : std_logic;
SIGNAL ww_clock : std_logic;
SIGNAL ww_q3 : std_logic;
SIGNAL ww_q2 : std_logic;
SIGNAL ww_q1 : std_logic;
SIGNAL ww_q0 : std_logic;
SIGNAL \clock~input_o\ : std_logic;
SIGNAL \q3~output_o\ : std_logic;
SIGNAL \q2~output_o\ : std_logic;
SIGNAL \q1~output_o\ : std_logic;
SIGNAL \q0~output_o\ : std_logic;
SIGNAL \b~input_o\ : std_logic;
SIGNAL \a~input_o\ : std_logic;
SIGNAL \q2~1_combout\ : std_logic;
SIGNAL \q2~2_combout\ : std_logic;
SIGNAL \q1~2_combout\ : std_logic;
SIGNAL \q1~1_combout\ : std_logic;
SIGNAL \q1~3_combout\ : std_logic;
SIGNAL \q2~3_combout\ : std_logic;
SIGNAL \q0~1_combout\ : std_logic;
SIGNAL \q0~2_combout\ : std_logic;
SIGNAL \q3~1_combout\ : std_logic;
SIGNAL \q3~2_combout\ : std_logic;

BEGIN

ww_a <= a;
ww_b <= b;
ww_clock <= clock;
q3 <= ww_q3;
q2 <= ww_q2;
q1 <= ww_q1;
q0 <= ww_q0;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;

-- Location: IOOBUF_X20_Y0_N9
\q3~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \q3~2_combout\,
	devoe => ww_devoe,
	o => \q3~output_o\);

-- Location: IOOBUF_X12_Y0_N9
\q2~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \q2~3_combout\,
	devoe => ww_devoe,
	o => \q2~output_o\);

-- Location: IOOBUF_X8_Y0_N2
\q1~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \q1~3_combout\,
	devoe => ww_devoe,
	o => \q1~output_o\);

-- Location: IOOBUF_X8_Y0_N9
\q0~output\ : cycloneiv_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \q0~2_combout\,
	devoe => ww_devoe,
	o => \q0~output_o\);

-- Location: IOIBUF_X10_Y0_N8
\b~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_b,
	o => \b~input_o\);

-- Location: IOIBUF_X14_Y0_N8
\a~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_a,
	o => \a~input_o\);

-- Location: LCCOMB_X9_Y1_N16
\q2~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q2~1_combout\ = (\q2~3_combout\) # ((\q3~2_combout\ & ((\a~input_o\))) # (!\q3~2_combout\ & (\b~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111110011101110",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \b~input_o\,
	datab => \q2~3_combout\,
	datac => \a~input_o\,
	datad => \q3~2_combout\,
	combout => \q2~1_combout\);

-- Location: LCCOMB_X9_Y1_N26
\q2~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q2~2_combout\ = (\q2~3_combout\) # (\q3~2_combout\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111111111001100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datab => \q2~3_combout\,
	datad => \q3~2_combout\,
	combout => \q2~2_combout\);

-- Location: LCCOMB_X9_Y1_N24
\q1~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q1~2_combout\ = (\q0~2_combout\ & ((\q1~3_combout\ & (\q3~2_combout\)) # (!\q1~3_combout\ & ((!\q2~3_combout\))))) # (!\q0~2_combout\ & ((\q3~2_combout\ & ((\q1~3_combout\))) # (!\q3~2_combout\ & (\q2~3_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1101110000011010",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \q0~2_combout\,
	datab => \q3~2_combout\,
	datac => \q2~3_combout\,
	datad => \q1~3_combout\,
	combout => \q1~2_combout\);

-- Location: LCCOMB_X9_Y1_N22
\q1~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q1~1_combout\ = (\q0~2_combout\ & (!\q3~2_combout\ & (\q2~3_combout\ & !\q1~3_combout\))) # (!\q0~2_combout\ & (((!\q2~3_combout\ & \q1~3_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000010100100000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \q0~2_combout\,
	datab => \q3~2_combout\,
	datac => \q2~3_combout\,
	datad => \q1~3_combout\,
	combout => \q1~1_combout\);

-- Location: LCCOMB_X9_Y1_N10
\q1~3\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q1~3_combout\ = (\q1~2_combout\ & (((\a~input_o\ & \q1~1_combout\)))) # (!\q1~2_combout\ & ((\b~input_o\) # ((!\q1~1_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1110001000110011",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \b~input_o\,
	datab => \q1~2_combout\,
	datac => \a~input_o\,
	datad => \q1~1_combout\,
	combout => \q1~3_combout\);

-- Location: LCCOMB_X9_Y1_N28
\q2~3\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q2~3_combout\ = (\q0~2_combout\ & (((\q2~2_combout\ & \q1~3_combout\)))) # (!\q0~2_combout\ & ((\q1~3_combout\ & (\q2~1_combout\)) # (!\q1~3_combout\ & ((\q2~2_combout\)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1110010001010000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \q0~2_combout\,
	datab => \q2~1_combout\,
	datac => \q2~2_combout\,
	datad => \q1~3_combout\,
	combout => \q2~3_combout\);

-- Location: LCCOMB_X9_Y1_N12
\q0~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q0~1_combout\ = (\q3~2_combout\ & (((!\q1~3_combout\)))) # (!\q3~2_combout\ & ((\q1~3_combout\) # ((\q0~2_combout\ & !\b~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0011001111001110",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \q0~2_combout\,
	datab => \q3~2_combout\,
	datac => \b~input_o\,
	datad => \q1~3_combout\,
	combout => \q0~1_combout\);

-- Location: LCCOMB_X9_Y1_N6
\q0~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q0~2_combout\ = (\q0~2_combout\ & ((\q2~3_combout\ & (!\q0~1_combout\)) # (!\q2~3_combout\ & ((!\q3~2_combout\))))) # (!\q0~2_combout\ & (\q0~1_combout\ $ (((!\q3~2_combout\) # (!\q2~3_combout\)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0100100100101111",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \q0~2_combout\,
	datab => \q2~3_combout\,
	datac => \q0~1_combout\,
	datad => \q3~2_combout\,
	combout => \q0~2_combout\);

-- Location: LCCOMB_X9_Y1_N0
\q3~1\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q3~1_combout\ = (\q3~2_combout\ & (\q0~2_combout\ $ (\q2~3_combout\ $ (\q1~3_combout\)))) # (!\q3~2_combout\ & (\q2~3_combout\ & ((\q0~2_combout\) # (\q1~3_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1011010001101000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \q0~2_combout\,
	datab => \q3~2_combout\,
	datac => \q2~3_combout\,
	datad => \q1~3_combout\,
	combout => \q3~1_combout\);

-- Location: LCCOMB_X9_Y1_N2
\q3~2\ : cycloneiv_lcell_comb
-- Equation(s):
-- \q3~2_combout\ = ((!\q0~2_combout\ & (\a~input_o\ & !\q2~3_combout\))) # (!\q3~1_combout\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0011001101110011",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \q0~2_combout\,
	datab => \q3~1_combout\,
	datac => \a~input_o\,
	datad => \q2~3_combout\,
	combout => \q3~2_combout\);

-- Location: IOIBUF_X14_Y31_N8
\clock~input\ : cycloneiv_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_clock,
	o => \clock~input_o\);

ww_q3 <= \q3~output_o\;

ww_q2 <= \q2~output_o\;

ww_q1 <= \q1~output_o\;

ww_q0 <= \q0~output_o\;
END structure;


