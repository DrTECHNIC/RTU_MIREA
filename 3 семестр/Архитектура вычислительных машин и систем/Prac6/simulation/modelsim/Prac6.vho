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

-- DATE "10/20/2024 14:18:15"

-- 
-- Device: Altera EPM240F100C4 Package FBGA100
-- 

-- 
-- This VHDL file should be used for ModelSim-Altera (VHDL) only
-- 

LIBRARY IEEE;
LIBRARY MAXII;
USE IEEE.STD_LOGIC_1164.ALL;
USE MAXII.MAXII_COMPONENTS.ALL;

ENTITY 	Prac6 IS
    PORT (
	q : OUT std_logic_vector(3 DOWNTO 0);
	clock : IN std_logic;
	a : IN std_logic;
	b : IN std_logic
	);
END Prac6;

-- Design Ports Information
-- q[3]	=>  Location: PIN_K5,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[2]	=>  Location: PIN_F1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[1]	=>  Location: PIN_J5,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- q[0]	=>  Location: PIN_F2,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
-- a	=>  Location: PIN_F3,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
-- clock	=>  Location: PIN_E1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
-- b	=>  Location: PIN_H4,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default


ARCHITECTURE structure OF Prac6 IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_q : std_logic_vector(3 DOWNTO 0);
SIGNAL ww_clock : std_logic;
SIGNAL ww_a : std_logic;
SIGNAL ww_b : std_logic;
SIGNAL \clock~combout\ : std_logic;
SIGNAL \a~combout\ : std_logic;
SIGNAL \inst24~7_combout\ : std_logic;
SIGNAL \inst24~6_combout\ : std_logic;
SIGNAL \b~combout\ : std_logic;
SIGNAL \inst24~4_combout\ : std_logic;
SIGNAL \inst24~3_combout\ : std_logic;
SIGNAL \inst24~8_combout\ : std_logic;
SIGNAL \inst28~regout\ : std_logic;
SIGNAL \inst36~4_combout\ : std_logic;
SIGNAL \inst29~regout\ : std_logic;
SIGNAL \inst23~7_combout\ : std_logic;
SIGNAL \inst23~6_combout\ : std_logic;
SIGNAL \inst23~4_combout\ : std_logic;
SIGNAL \inst23~3_combout\ : std_logic;
SIGNAL \inst23~8_combout\ : std_logic;
SIGNAL \inst27~regout\ : std_logic;
SIGNAL \inst22~4_combout\ : std_logic;
SIGNAL \inst26~regout\ : std_logic;

BEGIN

q <= ww_q;
ww_clock <= clock;
ww_a <= a;
ww_b <= b;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;

-- Location: PIN_E1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\clock~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_clock,
	combout => \clock~combout\);

-- Location: PIN_F3,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\a~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_a,
	combout => \a~combout\);

-- Location: LC_X4_Y2_N7
\inst24~7\ : maxii_lcell
-- Equation(s):
-- \inst24~7_combout\ = (\inst29~regout\ & ((\inst28~regout\ & (!\inst26~regout\)) # (!\inst28~regout\ & ((\inst26~regout\) # (\inst27~regout\))))) # (!\inst29~regout\ & (\inst27~regout\ $ (((\inst28~regout\) # (!\inst26~regout\)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "5c6b",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst28~regout\,
	datab => \inst29~regout\,
	datac => \inst26~regout\,
	datad => \inst27~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~7_combout\);

-- Location: LC_X4_Y2_N6
\inst24~6\ : maxii_lcell
-- Equation(s):
-- \inst24~6_combout\ = (\inst28~regout\ & ((\inst26~regout\ & (!\inst27~regout\ & !\inst29~regout\)) # (!\inst26~regout\ & ((\inst29~regout\))))) # (!\inst28~regout\ & (\inst26~regout\ $ (((!\inst27~regout\ & !\inst29~regout\)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "6649",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst28~regout\,
	datab => \inst26~regout\,
	datac => \inst27~regout\,
	datad => \inst29~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~6_combout\);

-- Location: PIN_H4,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: Default
\b~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "input")
-- pragma translate_on
PORT MAP (
	oe => GND,
	padio => ww_b,
	combout => \b~combout\);

-- Location: LC_X4_Y2_N0
\inst24~4\ : maxii_lcell
-- Equation(s):
-- \inst24~4_combout\ = (\inst27~regout\ & ((\inst26~regout\ & (!\inst28~regout\)) # (!\inst26~regout\ & ((\inst29~regout\))))) # (!\inst27~regout\ & (\inst26~regout\ $ (((\inst28~regout\) # (!\inst29~regout\)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "7643",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst28~regout\,
	datab => \inst26~regout\,
	datac => \inst27~regout\,
	datad => \inst29~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~4_combout\);

-- Location: LC_X4_Y2_N3
\inst24~3\ : maxii_lcell
-- Equation(s):
-- \inst24~3_combout\ = (\inst28~regout\ & (!\inst26~regout\ & ((\inst29~regout\)))) # (!\inst28~regout\ & (\inst26~regout\ $ (((!\inst27~regout\ & !\inst29~regout\)))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "6641",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst28~regout\,
	datab => \inst26~regout\,
	datac => \inst27~regout\,
	datad => \inst29~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~3_combout\);

-- Location: LC_X4_Y2_N4
\inst24~8\ : maxii_lcell
-- Equation(s):
-- \inst24~8_combout\ = (\b~combout\ & ((\a~combout\) # ((\inst24~4_combout\)))) # (!\b~combout\ & (!\a~combout\ & ((\inst24~3_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "b9a8",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \b~combout\,
	datab => \a~combout\,
	datac => \inst24~4_combout\,
	datad => \inst24~3_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst24~8_combout\);

-- Location: LC_X4_Y2_N5
inst28 : maxii_lcell
-- Equation(s):
-- \inst28~regout\ = DFFEAS((\a~combout\ & ((\inst24~8_combout\ & (\inst24~7_combout\)) # (!\inst24~8_combout\ & ((\inst24~6_combout\))))) # (!\a~combout\ & (((\inst24~8_combout\)))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "dda0",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \a~combout\,
	datab => \inst24~7_combout\,
	datac => \inst24~6_combout\,
	datad => \inst24~8_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst28~regout\);

-- Location: LC_X3_Y2_N2
\inst36~4\ : maxii_lcell
-- Equation(s):
-- \inst36~4_combout\ = (\inst29~regout\ & (!\inst26~regout\ & ((\b~combout\) # (!\inst27~regout\)))) # (!\inst29~regout\ & (((\inst26~regout\) # (\inst27~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "5d5a",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst29~regout\,
	datab => \b~combout\,
	datac => \inst26~regout\,
	datad => \inst27~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst36~4_combout\);

-- Location: LC_X3_Y2_N3
inst29 : maxii_lcell
-- Equation(s):
-- \inst29~regout\ = DFFEAS((\inst27~regout\ & ((\inst28~regout\ & (\inst26~regout\ & !\inst36~4_combout\)) # (!\inst28~regout\ & ((\inst36~4_combout\))))) # (!\inst27~regout\ & ((\inst28~regout\ & ((\inst36~4_combout\))) # (!\inst28~regout\ & 
-- (!\inst26~regout\)))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "6781",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst27~regout\,
	datab => \inst28~regout\,
	datac => \inst26~regout\,
	datad => \inst36~4_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst29~regout\);

-- Location: LC_X3_Y2_N0
\inst23~7\ : maxii_lcell
-- Equation(s):
-- \inst23~7_combout\ = (\inst29~regout\ & (\inst28~regout\ & ((\inst27~regout\) # (\inst26~regout\)))) # (!\inst29~regout\ & ((\inst27~regout\) # ((\inst26~regout\) # (\inst28~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "fd54",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst29~regout\,
	datab => \inst27~regout\,
	datac => \inst26~regout\,
	datad => \inst28~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst23~7_combout\);

-- Location: LC_X3_Y2_N4
\inst23~6\ : maxii_lcell
-- Equation(s):
-- \inst23~6_combout\ = (\inst29~regout\ & (\inst28~regout\ & ((\inst27~regout\) # (\inst26~regout\)))) # (!\inst29~regout\ & ((\inst27~regout\) # ((\inst26~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "fc54",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst29~regout\,
	datab => \inst27~regout\,
	datac => \inst26~regout\,
	datad => \inst28~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst23~6_combout\);

-- Location: LC_X3_Y2_N5
\inst23~4\ : maxii_lcell
-- Equation(s):
-- \inst23~4_combout\ = (\inst29~regout\ & (\inst28~regout\ & ((\inst27~regout\) # (\inst26~regout\)))) # (!\inst29~regout\ & ((\inst27~regout\) # (\inst26~regout\ $ (\inst28~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "ed54",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst29~regout\,
	datab => \inst27~regout\,
	datac => \inst26~regout\,
	datad => \inst28~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst23~4_combout\);

-- Location: LC_X3_Y2_N7
\inst23~3\ : maxii_lcell
-- Equation(s):
-- \inst23~3_combout\ = (\inst27~regout\ & (((\inst28~regout\)) # (!\inst29~regout\))) # (!\inst27~regout\ & (\inst26~regout\ & (\inst29~regout\ $ (!\inst28~regout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "ec54",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst29~regout\,
	datab => \inst27~regout\,
	datac => \inst26~regout\,
	datad => \inst28~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst23~3_combout\);

-- Location: LC_X3_Y2_N8
\inst23~8\ : maxii_lcell
-- Equation(s):
-- \inst23~8_combout\ = (\b~combout\ & ((\a~combout\) # ((\inst23~4_combout\)))) # (!\b~combout\ & (!\a~combout\ & ((\inst23~3_combout\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "b9a8",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \b~combout\,
	datab => \a~combout\,
	datac => \inst23~4_combout\,
	datad => \inst23~3_combout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst23~8_combout\);

-- Location: LC_X3_Y2_N9
inst27 : maxii_lcell
-- Equation(s):
-- \inst27~regout\ = DFFEAS((\a~combout\ & ((\inst23~8_combout\ & (\inst23~7_combout\)) # (!\inst23~8_combout\ & ((\inst23~6_combout\))))) # (!\a~combout\ & (((\inst23~8_combout\)))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "dda0",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \a~combout\,
	datab => \inst23~7_combout\,
	datac => \inst23~6_combout\,
	datad => \inst23~8_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst27~regout\);

-- Location: LC_X4_Y2_N1
\inst22~4\ : maxii_lcell
-- Equation(s):
-- \inst22~4_combout\ = (\inst28~regout\ & ((\inst29~regout\ & ((!\inst27~regout\))) # (!\inst29~regout\ & ((\a~combout\) # (\inst27~regout\))))) # (!\inst28~regout\ & (!\inst29~regout\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "33b9",
	operation_mode => "normal",
	output_mode => "comb_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	dataa => \inst28~regout\,
	datab => \inst29~regout\,
	datac => \a~combout\,
	datad => \inst27~regout\,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	combout => \inst22~4_combout\);

-- Location: LC_X4_Y2_N2
inst26 : maxii_lcell
-- Equation(s):
-- \inst26~regout\ = DFFEAS((\inst26~regout\ & (\inst22~4_combout\ $ (((\inst27~regout\ & !\inst28~regout\))))) # (!\inst26~regout\ & (((!\inst28~regout\ & \inst22~4_combout\)) # (!\inst27~regout\))), GLOBAL(\clock~combout\), VCC, , , , , , )

-- pragma translate_off
GENERIC MAP (
	lut_mask => "b719",
	operation_mode => "normal",
	output_mode => "reg_only",
	register_cascade_mode => "off",
	sum_lutc_input => "datac",
	synch_mode => "off")
-- pragma translate_on
PORT MAP (
	clk => \clock~combout\,
	dataa => \inst26~regout\,
	datab => \inst27~regout\,
	datac => \inst28~regout\,
	datad => \inst22~4_combout\,
	aclr => GND,
	devclrn => ww_devclrn,
	devpor => ww_devpor,
	regout => \inst26~regout\);

-- Location: PIN_K5,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[3]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst26~regout\,
	oe => VCC,
	padio => ww_q(3));

-- Location: PIN_F1,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[2]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst27~regout\,
	oe => VCC,
	padio => ww_q(2));

-- Location: PIN_J5,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[1]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst28~regout\,
	oe => VCC,
	padio => ww_q(1));

-- Location: PIN_F2,	 I/O Standard: 3.3-V LVTTL,	 Current Strength: 16mA
\q[0]~I\ : maxii_io
-- pragma translate_off
GENERIC MAP (
	operation_mode => "output")
-- pragma translate_on
PORT MAP (
	datain => \inst29~regout\,
	oe => VCC,
	padio => ww_q(0));
END structure;


