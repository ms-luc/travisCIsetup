
class Main:

    variable_01 = "01"
    variable_02 = "02"
    variable_03 = "03"
    variable_04 = "04"
	
    def function_01(var1, var2):
        print(var1, var2)
		
    def function_02(var1, var2):
        print("%s\n%s" % (var1, var2))
		

Main.function_01(Main.variable_01, Main.variable_02)
Main.function_02(Main.variable_01, Main.variable_02)
Main.function_02(Main.variable_03, Main.variable_04)
Main.function_02(Main.variable_03, Main.variable_04)
