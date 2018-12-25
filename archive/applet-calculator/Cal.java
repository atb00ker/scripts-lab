import java.applet.*;
import java.awt.event.*;
import java.awt.*;
import java.util.Stack;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Cal extends Applet implements ActionListener {

	Label lblcalc = new Label("Calculator");
	String equation = " ";
	TextField textField = new TextField(30);


	Button seven = new Button("7");
	Button eight = new Button("8");
	Button nine = new Button("9");
	Button DEL = new Button("DEL");
	Button AC = new Button("CLEAR");

	Button four = new Button("4");
	Button five = new Button("5");
	Button six = new Button("6");
	Button multiply = new Button("x");
	Button subtract = new Button("-");

	Button one = new Button("1");
	Button two = new Button("2");
	Button three = new Button("3");
	Button plus = new Button("+");
	Button dive = new Button("/");

	Button zero = new Button("0");
	Button equals = new Button("=");


	public void init() {

		setLayout(null);

		Font calcText= new Font("Serif",Font.BOLD,18);
		lblcalc.setFont(calcText);

		add(lblcalc);
		add(textField);

		add(seven);
		add(eight);
		add(nine);
		add(DEL);
		add(AC);

		add(four);
		add(five);
		add(six);
		add(multiply);
		add(subtract);

		add(one);
		add(two);
		add(three);
		add(plus);
		add(dive);

		add(zero);
		add(equals);

		lblcalc.setBounds(60,0,100,20);
		textField.setBounds(100,50,240,20);


		seven.setBounds(100,165,35,35);
		eight.setBounds(150,165,35,35);
		nine.setBounds(200,165,35,35);
		AC.setBounds(250,165,85,35);

		four.setBounds(100,210,35,35);
		five.setBounds(150,210,35,35);
		six.setBounds(200,210,35,35);
		multiply.setBounds(250,210,35,35);
		subtract.setBounds(300,210,35,35);

		one.setBounds(100,255,35,35);
		two.setBounds(150,255,35,35);
		three.setBounds(200,255,35,35);
		plus.setBounds(250,255,35,35);
		dive.setBounds(300,255,35,35);

		zero.setBounds(100,300,35,35);
		equals.setBounds(150,300,85,35);


		equals.addActionListener(this);
		one.addActionListener(this);
		two.addActionListener(this);
		three.addActionListener(this);
		plus.addActionListener(this);
		dive.addActionListener(this);
		four.addActionListener(this);
		five.addActionListener(this);
		six.addActionListener(this);
		multiply.addActionListener(this);
		subtract.addActionListener(this);
		seven.addActionListener(this);
		eight.addActionListener(this);
		nine.addActionListener(this);
		AC.addActionListener(this);
		zero.addActionListener(this);
		textField.setEnabled(false);

	}

	
	public void actionPerformed(ActionEvent customEvent) {
		String buttonPressed = customEvent.getActionCommand();
		if (buttonPressed.equals("=")) {
            String result = "";
			for (int i = 0; i < equation.length(); i++) {    
				char c = equation.charAt(i);
   				if (c >= '0' && c <= '9') {
					result += Character.toString(c);
				} else {
					result += " " + Character.toString(c) + " ";
				}
			}
			equation = String.valueOf(EvaluateDynamicString.evaluate(result));
 		} else if (buttonPressed.equals("CLEAR")) {
			equation = " ";
		} else {
			equation = equation.concat(buttonPressed);
		}
		textField.setText(equation);
	}
}

 
class EvaluateDynamicString {

    public static int evaluate(String expression) {
        char[] tokens = expression.toCharArray();
        Stack<Integer> values = new Stack<Integer>();
        Stack<Character> operands = new Stack<Character>(); 
        for (int i = 0; i < tokens.length; i++) {
            if (tokens[i] == ' ')
                continue;
            if (tokens[i] >= '0' && tokens[i] <= '9') {
                StringBuffer sbuf = new StringBuffer();
                while (i < tokens.length && tokens[i] >= '0' && tokens[i] <= '9')
                    sbuf.append(tokens[i++]);
                values.push(Integer.parseInt(sbuf.toString()));
            } else if (tokens[i] == '(')
                operands.push(tokens[i]);
            else if (tokens[i] == ')') {
                while (operands.peek() != '(')
                  values.push(applyAction(operands.pop(), values.pop(), values.pop()));
                operands.pop();
			} else if (tokens[i] == '+' || tokens[i] == '-' || tokens[i] == '*' || tokens[i] == '/') {
                while (!operands.empty() && openBrackets(tokens[i], operands.peek()))
                  values.push(applyAction(operands.pop(), values.pop(), values.pop()));
                operands.push(tokens[i]);
            }
        }
        while (!operands.empty())
            values.push(applyAction(operands.pop(), values.pop(), values.pop()));
        return values.pop();
    }
    
	
	public static boolean openBrackets(char operand1, char operand2) {
        if (operand2 == '(' || operand2 == ')')
            return false;
        if ((operand1 == '*' || operand1 == '/') && (operand2 == '+' || operand2 == '-'))
            return false;
        else
            return true;
    }


    public static int applyAction(char operand, int b, int a) {
        switch (operand)
        {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            if (b == 0)
                throw new
                UnsupportedOperationException("Cannot divide by zero");
            return a / b;
        }
        return 0;
    }
}
