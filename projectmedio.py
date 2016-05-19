import sys

from PySide.QtCore import*
from PySide.QtGui import*
from PySide.QtUiTools import*

class userclientgui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)
        self.imagelogo = QPixmap("medio login.png");
        self.loader = QUiLoader();
        form = self.loader.load("C:/Users/por_n/Documents/SEP project UI/loginregistered.ui",self);
        self.setCentralWidget(form);
        self.background = form.findChild(QLabel,"label") ;
        self.image = QPixmap("bgb.png");
        self.background.setPixmap(self.image);
        self.background.show();       
        button1 = form.findChild(QPushButton,"pushButton");
        button1.setIcon(QIcon("medio login.png"));
        button1.clicked.connect(self.tologinscreen);
    
    def tologinscreen(self):
        form2 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/log in mock up ui.ui",self);
        self.setCentralWidget(form2);
        self.background = form2.findChild(QLabel,"background");
        acclevel = form2.findChild(QComboBox,"acclevel");
        cslevel = form2.findChild(QLabel,"cslevel");
        self.keeplog = form2.findChild(QCheckBox,"keeplog");
        keeplogl = form2.findChild(QLabel,"keeplogl");
        logo = form2.findChild(QLabel,"logo");
        notres = form2.findChild(QLabel,"notres");
        self.passfield = form2.findChild(QLineEdit,"passfield");
        password = form2.findChild(QLabel,"password");
        self.remuser = form2.findChild(QCheckBox,"remuser");
        remuserl = form2.findChild(QLabel,"remuserl");
        self.userfield = form2.findChild(QLineEdit,"userfield");
        username = form2.findChild(QLabel,"username");
        loginb = form2.findChild(QPushButton,"login") 
        cancel = form2.findChild(QPushButton,"cancel");
        registerhere = form2.findChild(QPushButton,"registerhere");
                
        self.background.setPixmap(self.image);
        self.background.show();       
        logo.setPixmap(self.imagelogo);
        logo.show();
        cancel.clicked.connect(self.backtofront);
        loginb.clicked.connect(self.login);
    def backtofront(self):
        self.timer.stop();
        form = self.loader.load("C:/Users/por_n/Documents/SEP project UI/loginregistered.ui",self);
        self.setCentralWidget(form);
        self.background = form.findChild(QLabel,"label") ;
        self.image = QPixmap("bgb.png");
        self.background.setPixmap(self.image);
        self.background.show();       
        button1 = form.findChild(QPushButton,"pushButton");
        button1.setIcon(QIcon("medio login.png"));
        button1.clicked.connect(self.tologinscreen);    
    def backtomainmenu(self):
        self.timer.stop();
        form3 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/mainmenu.ui",self);
        self.setCentralWidget(form3);
        self.background = form3.findChild(QLabel,"background") ;
        self.image = QPixmap("Mainmenubg.png");
        self.background.setPixmap(self.image);
        button1 = form3.findChild(QPushButton,"appointment");
        button1.setIcon(QIcon("main button.png"));
        button1.clicked.connect(self.toappointment1); 
        button2 = form3.findChild(QPushButton,"medsche");
        button2.setIcon(QIcon("medicineschedulebutton.png"));
        button2.clicked.connect(self.tomedschedulemonth); 
        button3 = form3.findChild(QPushButton,"transac");
        button3.setIcon(QIcon("Historybutton.png"));
        button4 = form3.findChild(QPushButton,"settings");
        button4.setIcon(QIcon("settingsbutton.png"));
        button5 = form3.findChild(QPushButton,"contact");
        button5.setIcon(QIcon("contactandclicktocallbutton.png")); 
    def login(self):
        inputusername = self.userfield.text();
        inputpassword = self.passfield.text();
        self.remuser.isChecked();
        print(self.remuser.isChecked())
        print(self.keeplog.isChecked())
        print(inputusername);
        print(inputpassword);
        testuserkey = ""
        testpasskey = ""
        if(inputusername == testuserkey and inputpassword == testpasskey):
            form3 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/mainmenu.ui",self);
            self.setCentralWidget(form3);
            self.background = form3.findChild(QLabel,"background") ;
            self.image = QPixmap("Mainmenubg.png");
            self.background.setPixmap(self.image);
            button1 = form3.findChild(QPushButton,"appointment");
            button1.setIcon(QIcon("main button.png"));
            button1.clicked.connect(self.toappointment1); 
            button2 = form3.findChild(QPushButton,"medsche");
            button2.setIcon(QIcon("medicineschedulebutton.png"));
            button2.clicked.connect(self.tomedschedulemonth); 
            button3 = form3.findChild(QPushButton,"transac");
            button3.setIcon(QIcon("Historybutton.png"));
            button4 = form3.findChild(QPushButton,"settings");
            button4.setIcon(QIcon("settingsbutton.png"));
            button5 = form3.findChild(QPushButton,"contact");
            button5.setIcon(QIcon("contactandclicktocallbutton.png")); 
        else:
            print("wrong username or password");
        
    def toappointment1(self):
        form3 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/appointmentscreen.ui",self);
        self.setCentralWidget(form3);
        self.background = form3.findChild(QLabel,"background");
        orth = form3.findChild(QPushButton,"Ortho");
        gastro = form3.findChild(QPushButton,"GI");  
        emer = form3.findChild(QPushButton,"ER");
        dermato = form3.findChild(QPushButton,"Derma");
        pedia = form3.findChild(QPushButton,"Ped");
        outpat = form3.findChild(QPushButton,"OPD");
        cardi = form3.findChild(QPushButton,"Cardio");
        neurology = form3.findChild(QPushButton,"Neuro");
        rad = form3.findChild(QPushButton,"Radio");
        back = form3.findChild(QPushButton,"backtomain");
        self.clocknow = form3.findChild(QLCDNumber,"clock");
        diviv = form3.findChild(QLine,"dividerverti");
        divih = form3.findChild(QLine,"dividerhori");
        self.image = QPixmap("bgb.png");
        self.background.setPixmap(self.image);
        orth.setIcon(QIcon("orthopedicbutton.png"));
        gastro.setIcon(QIcon("GIbutton.png"));
        emer.setIcon(QIcon("ERbutton.png"));
        dermato.setIcon(QIcon("dermatologybutton.png"));
        pedia.setIcon(QIcon("pedibutton.png"));
        outpat.setIcon(QIcon("opdbutton.png"));
        cardi.setIcon(QIcon("cardiologybutton.png"));
        neurology.setIcon(QIcon("neurologybutton.png"));
        rad.setIcon(QIcon("radiologybutton.png"));
        back.setIcon(QIcon("returnbutton.png"));
        
        back.clicked.connect(self.backtomainmenu); 
            
        self.clocknow.setSegmentStyle(QLCDNumber.Filled);

        self.timer = QTimer();
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000);
    def showtime(self):
        self.time = QTime.currentTime();
        self.text = self.time.toString("hh:mm");
        self.clocknow.display(self.text);
    def tomedschedulemonth(self):
        form4 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/medicineschedulescreen.ui",self);
        self.setCentralWidget(form4);
        self.background = form4.findChild(QLabel,"background");
        addmed = form4.findChild(QPushButton,"add");
        dele = form4.findChild(QPushButton,"delmed");
        sd = form4.findChild(QPushButton,"setday");
        cv = form4.findChild(QPushButton,"changelook");
        cal  = form4.findChild(QCalendarWidget,"calendar");
        back = form4.findChild(QPushButton,"backbutton");
        self.image = QPixmap("bgb.png");
        self.background.setPixmap(self.image);
        
        addmed.setIcon(QIcon("addmedbutton.png"));
        dele.setIcon(QIcon("deletemedicinebutton.png"));
        sd.setIcon(QIcon("setdatebutton.png"));
        cv.setIcon(QIcon("changeviewbutton.png"));
        back.setIcon(QIcon("returnbutton.png"));

        back.clicked.connect(self.backtomainmenu);         
        cv.clicked.connect(self.tomedscheduleweek);         

        self.clocknow  = form4.findChild(QLCDNumber,"clock");
        
        self.timer = QTimer();
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000);
    def tomedscheduleweek(self):
        form4 = self.loader.load("C:/Users/por_n/Documents/SEP project UI/medicinescheduleweekview.ui",self);
        self.setCentralWidget(form4);
        self.background = form4.findChild(QLabel,"background");
        addmed = form4.findChild(QPushButton,"add");
        dele = form4.findChild(QPushButton,"delmed");
        sd = form4.findChild(QPushButton,"setday");
        cv = form4.findChild(QPushButton,"changelook");
        cal  = form4.findChild(QCalendarWidget,"calendar");
        back = form4.findChild(QPushButton,"backbutton");
        self.image = QPixmap("bgb.png");
        self.background.setPixmap(self.image);
        head = form4.findChild(QLabel,"header");
        mon1 = form4.findChild(QLabel,"monday");
        mon2 = form4.findChild(QListWidget,"mondaylist");
        tue1 = form4.findChild(QLabel,"tuesday");
        tue2 = form4.findChild(QListWidget,"tuesdaylist");
        wed1 = form4.findChild(QLabel,"wednesday");
        wed2 = form4.findChild(QListWidget,"wednesdaylist");
        thur1 = form4.findChild(QLabel,"thursday");
        thur2 = form4.findChild(QListWidget,"thursdaylist");
        fri1 = form4.findChild(QLabel,"friday"); 
        fri2 = form4.findChild(QListWidget,"fridaylist");
        sat1 = form4.findChild(QLabel,"saturday");
        sat2 = form4.findChild(QListWidget,"saturdaylist");
        sun1 = form4.findChild(QLabel,"sunday");
        sun2 = form4.findChild(QListWidget,"sundaylist");
        addmed.setIcon(QIcon("addmedbutton.png"));
        dele.setIcon(QIcon("deletemedicinebutton.png"));
        sd.setIcon(QIcon("setdatebutton.png"));
        cv.setIcon(QIcon("changeviewbutton.png"));
        back.setIcon(QIcon("returnbutton.png"));
        image1 = QPixmap("medbanner.png");
        image2 = QPixmap("monday.png");
        image3 = QPixmap("tuesday.png");
        image4 = QPixmap("wednesday.png");
        image5 = QPixmap("thursday.png");
        image6 = QPixmap("friday.png");
        image7 = QPixmap("saturday.png");
        image8 = QPixmap("sunday.png");        
        head.setPixmap(image1);
        mon1.setPixmap(image2);
        tue1.setPixmap(image3);
        wed1.setPixmap(image4);
        thur1.setPixmap(image5);
        fri1.setPixmap(image6);
        sat1.setPixmap(image7);
        sun1.setPixmap(image8);
        
        back.clicked.connect(self.backtomainmenu); 
        cv.clicked.connect(self.tomedschedulemonth);         

        self.clocknow  = form4.findChild(QLCDNumber,"clock");
        
        self.timer = QTimer();
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000);
        
class GUIobserver:
    def __init__(self, **kwargs):             
        self.guiuser = userclientgui()
        self.guiuser.show()
    def getuserfield(self):
        inputusername = self.guiuser.userfield.text();
        return inputusername
    def getpassfield(self):
        inputpassword = self.guiuser.passfield.text();
        return inputpassword
    def getkeepusernamestatus(self):
        return self.guiuser.remuser.isChecked()
    def getkeeploggedinstatus(self):
        return self.guiuser.keeplog.isChecked()

def main():
    
    app = QApplication(sys.argv)
    observer1 = GUIobserver()

    return app.exec_()
if __name__=="__main__":
    sys.exit(main())