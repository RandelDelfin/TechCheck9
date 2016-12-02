import sys
from techcheck9 import *


#import generated UI file here


class MyForm(QtWidgets.QMainWindow):


        #DO NOT MODIFY THIS SECTION OF CODE
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #END DO NOT MODIFY

        # ADD SLOTS HERE
        self.ui.pushButtonCalculate.clicked.connect(self.CalculateButton)

    # ADD SLOT FUNCTIONS HERE
    def CalculateButton(self):
        salary = float(self.ui.lineeditSalary.text())
        dependents = float(self.ui.lineEditDependents.text())


        federal = salary * 0.25
        provincial = salary * 0.06
        dependent_deduction = salary * (dependents * 0.02)
        total = salary - federal - provincial + dependent_deduction

        labeloutput = "Your Federal Tax is: $%.2f\n"% federal
        labeloutput += "Your Provincial Tax is: $%.2f\n"% provincial
        labeloutput += "Your Dependent Tax is: $%.2f\n"% dependent_deduction
        labeloutput += "Your Total take-home pay is: $%.2f\n"% total

        self.ui.labelOutput.setText(labeloutput)



    # ADD ALL OTHER HELPER FUNCTIONS HERE


#DO NOT MODIFY THIS SECTION OF CODE
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
#END DO NOT MODIFY
