## 2021 Project 2

![](logo.png)

Ερωτήσεις:

1. Πού βρίσκεται ο Γιώργος;
1. Ποιος έκλεψε τα αρχεία του "Plan X";
1. Πού βρίσκονται τα αρχεία του "Plan X";
1. Ποια είναι τα results του "Plan Y";
1. Ποιο είναι το code του "Plan Z";


#### Παρατηρήσεις

- Οι ίδιες ομάδες με την εργασία 1
- Εγγραφή στο github: https://classroom.github.com/g/jlkOQHdH 
- Μόλις ολοκληρώσετε κάθε βήμα στέλνετε claim στο ys13@chatzi.org
- Για τα βήματα 3-5 απαιτείται να γράψετε ένα πρόγραμμα που να αυτοματοποιεί την εύρεση της λύσης.
  Μπορείτε να χρησιμοποιήσετε ό,τι γλώσσα προγραμματισμού θέλετε, αλλά θα πρέπει να μπορώ να το τρέξω
  σε Ubuntu 20.04 χρησιμοποιώντας software που είναι διαθέσιμο στο Ubuntu. Θα πρέπει επίσης
  να φτιάξετε ένα script `run.sh` που εκτελεί το πρόγραμμα με ό,τι παραμέτρους χρειάζονται.
- Επίσης γράφετε report στο README.md με τα βήματα που ακολουθήσατε, και το κάνετε commit μαζί με οποιοδήποτε κώδικα χρησιμοποιήσατε
- Βαθμολογία
    - Η δυσκολία στα βήματα αυξάνεται απότομα.
    - Για ό,τι δεν ολοκληρώσετε περιγράψτε (και υλοποιήστε στο πρόγραμμα) την πρόοδό σας και πώς θα μπορούσατε να συνεχίσετε.
    - Με τα πρώτα 2 βήματα παίρνετε 5 στο μάθημα (αν έχετε πάει καλά στην εργασία 1)
    - Με τα 3-5 φτάνετε μέχρι το 10 (δεν υπάρχει γραπτή εξέταση)
    - Για τους μεταπτυχιακούς τα 3-5 είναι προαιρετικά. ΔΕΝ αντικαθιστούν το project
     (αλλά μπορούν να λειτουργήσουν προσθετικά στο βαθμό της εργασίας 1)
    - Για τα βήματα 3-5 μπορεί να γίνει προφορική εξέταση
- Timeline
    - Την πρώτη εβδομάδα δεν υπάρχουν hints
    - 11/6: αρχίζουν τα hints για τα βήματα 1,2
    - 16/6: deadline για τα βήματα 1,2
    - Για τα βήματα 3-5 δίνονται hints μόνο σε όσους ζητήσουν (με μικρό penalty)
    - 11/7: deadline για τα βήματα 3-5
- Η ταχύτητα των λύσεων (και ο αριθμός hints που έχουν δοθεί) μετράει στο βαθμό
(ειδικά για τα βήματα 1,2)

- __Οχι spoilers__
- __Οχι DoS__ (ή μαζικά requests, δε χρειάζεται
κάτι τέτοιο)

#### Ερώτημα 1
- Ξεκινήσαμε με επίσκεψη στο .onion που φαίνεται στην φωτογραφία της εκφώνησης.
- Εκεί ανοίξαμε τα dev tools και στον inspector βρήκαμε ένα σχόλιο μέσα στο οποίο υπήρχε link για ένα medium με τρόπους για να ασφαλίσεις .omion sites.            https://blog.0day.rocks/securing-a-web-hidden-service-89d935ba1c1d
- Σε αυτό το link στο 3.1) διαβάσαμε για τα server-status και server-info.
- Δοκιμάσαμε το server-status χωρίς επιτυχία, αλλά το server-info δούλεψε.
- Στο server-info βρήκαμε ένα δεύτερο onion domain το http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/. Επίσης βρήκαμε ότι το directory listing είναι enabled ( θα μας χρειαστεί αργότερα)
- Εκεί προσπαθήσαμε να μπούμε και παρατηρήσαμε ότι καλούσε το access.php
- Προσπαθώντας να βρούμε τι άλλα αρχεία μπορούμε να δούμε δοκιμάσαμε να μπούμε στο robots.txt
- Εκεί είδαμε ότι κάνει disallow αρχεία τύπου .phps
- Δοκιμάσαμε το access.phps και βρήκαμε τον κώδικα του access.php
- Για να βρούμε το desired χρησιμοποιήσαμε αύτο το [script](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/scripts/sevens.py)
- Για τον κωδικό βρήκαμε ότι η strcmp έχει ένα vulnerability στο οποίο αν κάνεις compare με empty array γυρνάει πάντα 0.Οπότε κάνοντας cast σε array το password, δοκιμάσαμε το http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/access.php/?user=0001337&password[] και δούλεψε.(στο 1337 προσθέσαμε 3 μηδενικά αφού ήθελε να έιναι μεγέθους 7).
- Εκεί βρήκαμε το blog στο http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/ και πατήσαμε στο diary που μας πήγε στο http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/diary.html. Ξέροντας ότι το directory listing είναι enabled δοκιμάσαμε το http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/ και στην σελίδα που μας άνοιξε πατήσαμε το post3.html το οπίο δεν είχαμε ξαναδεί.Εκεί διαβάσαμε για τον visitor #834472 στο site των fixers και ξαναγυρίσαμε πίσω.
- Στο site των fixers παρατηρήσαμε ότι αν κάνουμε reload τότε στο visitor number γράφει 204.Άρα το 204 προκύπτει άπο κάποιο cookie που μας δόθηκε την πρώτη φορά που μπήκαμε.
- Το cookie που βρήκαμε ήταν το MjA0OmZjNTZkYmM2ZDQ2NTJiMzE1Yjg2YjcxYzhkNjg4YzFjY2RlYTljNWYxZmQwNzc2M2QyNjU5ZmRlMmUyZmM0OWE.
- Δοκιμάσαμε να το κάνουμε decrypt χωρίς να ξέρουμε τι encryption απλά δοκιμάζοντας όλες τις διαθέσιμες επιλογές στο https://emn178.github.io/online-tools/base64_decode.html. Με base64 βρήκαμε 204:fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a. Έπειτα έπρεπε να βρούμε τι είναι το fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a. Έχοντας κοιτάξει και τον κώδικα του pico έιδαμε ότι για username και passwords στην check_authenticate φτιάχνει το base64(username:sha256(password)).Άρα το fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a μαντέψαμε ότι είναι κάτι encrypted σε sha-256.Ξέροντας ότι δεν μπορούμε να το κάνουμε decrypt ξεκινήσαμε δοκιμάζοντας με ό,τι στοιχείο έχουμε. ξεκινόντας με το 834472, το οποίο ήταν και το σωστό.Άρα στο τέλος φτιάξαμε το base64(834472:sha256(834472)) που είναι το ODM0NDcyOjI3YzNhZjdlZjJiZWUxYWY1MjdkYmY4YzA1YjNkYjZjY2E2MzU4OTk0MWI4ZDQ5NTcyYWE2NGI1Y2Q4YzViOTc=.
- Σετάραμε το νεο cookie και βγήκε το μήνυμα  Congrats user #834472!! Check directory /sekritbackup1843 for latest news... 
- Πήγαμε στην σελίδα http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion/sekritbackup1843/ όπου βρήκαμε δύο gpg αρχεία και το notes.txt.Στα notes διαβάσαμε για το πώς φτιάνχει το κλειδί για το gpg encryption.Επίσης στην τελευταία γραμμή το είχε ένα transaction hash μαζί με το ropsten.Κάνοντας search στο etherscan το transaction hash.Στο https://ropsten.etherscan.io/tx/0xdcf1bfb1207e9b22c77de191570d46617fe4cdf4dbc195ade273485dddc16783 βρήκαμε το bigtent στο input data ( UTF-8).Δοκιμάσαμε όλες τις ημερομηνίες ξεκινώντας από 01-01-2021 με αυτό το [script](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/scripts/decodeGpgFiles.py) και το βρήκαμε!
- Στο firefox.log βρήκαμε με αυτό το [script](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/scripts/findTheLink.py) ένα repo στο οποίο ψάξαμε το commit hash που βρήκαμε στο signal.log.
- Σε αυτό το commit https://github.com/asn-d6/tor/commit/4ec3bbea5172e13552d47ff95e02230e6dc99692 βλέποντας το N,e καταλάβαμε ότι έχουμε να κάνουμε με rsa.Με αυτό το [script](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/scripts/script.py) κάναμε decrypt και βρήκαμε τα x και y.Τα p και q τα βρήκαμε στο wolfram λύνοντας την εξίσωση N = (p-1)(q-1).
- Πηγαίνοντας τώρα στο http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/30637353063735.txt βρήκαμε ότι ο Γιώργος βρίσκεται στο Kilimanjaro.


### Ερώτημα 2

- Αρχικά απο τη σελίδα [blogposts7589109238/blogposts/diary2.html](http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/diary2.html) βρήκαμε πως ο server Plan X είναι στο link [zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion](zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion) και πως ο πηγαίος κώδικας του server ειναι ο [chatziko/pico](https://github.com/chatziko/pico), τον οποίο και ελέγξαμε.
- Στο αρχείο [main.c](https://github.com/chatziko/pico/blob/master/main.c) παρατηρήσαμε το σχόλιο "// TODO: gcc 7 gives warnings, check" στη γραμμή 25, οπότε κατεβάσαμε και εκτελέσαμε το pico τοπικά σε υπολογιστή μας.
- Φαίνεται πως το warning αφορά την εντολή "printf(auth_username)" στη γραμμή 135 του ίδιου αρχείου. Η εντολή printf δεν περιέχει format προς εκτύπωση ενώ τυπώνει το auth_username. Αναζητώντας αυτή τη περίπτωση στο internet καταλήξαμε στα παρακάτω site:
- https://stackoverflow.com/questions/31290850/why-is-printf-with-a-single-argument-without-conversion-specifiers-deprecated
- https://en.wikipedia.org/wiki/Uncontrolled_format_string
- Παρατηρήσαμε πως μπορούμε να εκμεταλευτούμε το Uncontrolled format string vulnerability και ίσως να τυπώσουμε περιεχόμενα των μεταβλητών με την εντολή "printf(auth_username)".
- Δίνοντας ως username διάφορους συνδυασμούς format που αποτελούνται απο "%x" (pop μεταβλητών απο τη στοίβα) και "%s" (εκτύπωση string μετά τα pop) παρατηρήσαμε πως δίνοντας ως είσοδο το username "%x %x %x %x %x %x %s" τυπώνεται η πρώτη συμβολοσειρά του πίνακα htpasswd, η οποία είναι η "admin:e5614e27f3c21283ad532a1d23b9e29d", και αποτελεί το username και hashed password του admin.
- Τελικά προσπαθήσαμε να βρούμε το reverse-hashed password του admin σε διάφορα md5-reverse εργαλεία στο internet και το βρήκαμε στο [site](https://md5.gromweb.com/?md5=e5614e27f3c21283ad532a1d23b9e29d), ο οποίος τελικά ήταν "bob's your uncle".
- Έτσι, αποκτήσαμε πρόσβαση στη σελίδα [http://zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion/](http://zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion/) και παρατηρήσαμε πως τα αρχεία του Plan X έκλεψαν οι 5l0ppy 8uff00n5.


### Ερώτημα 3

(Για το ερώτημα 3 λάβαμε hint το οποίο ήρθε 5 μέρες μετά που το ζητήσαμε.Όπως γράψαμε και στο reply,στο ενδιάμεσο είχαμε βρει ήδη το πρόβλημα, το οποίο ήταν ότι μεταγλωτίζαμε το pico σε 64bit)

#### Content Length

Για το ερώτημα 3 αρχικά μελετήσαμε σε βάθος τον κώδικα του pico.Εκεί βρήκαμε την συνάρτηση serve_ultimate()
που καλείται αν πετύχει το authentication στην post_param.Έχοντας παρακολουθήσει τις διαλέξεις του μαθήματος,
μαντέψαμε ότι θα χρειαστεί να κάνουμε κάποιο buffer overflow.Το request που στέλνεται όταν προσπαθούμε να κάνουμε
post στο .../ultimate.html είχε data raw της μορφής "admin=<given pass>&submit=go".Μελετώντας τον κώδικα του pico
είδαμε πως αυτό το payload το αποθήκευε με strcpy στο post_data στην post_param().Εκεί είδαμε ότι δίνει μέγεθος
στο post_data ίσο με payload_size+1.Το payload_size όμως είχε το πρόβλημα ότι σε περίπτωση που το request είχε header
Content-Length, τότε έπαιρνε εκείνη την τιμή και όχι υπολογίζοντας το μέγεθος του ίδιου του payload.Έτσι βρήκαμε το πρώτο
βήμα για το buffer overflow, δηλαδή μπορούσαμε να γράψουμε στο stack πέρα του χώρου που είχε δωθεί στο post_data.Αυτό το 
καταφέρναμε βάζωντας Content-Length < actual payload_size.

#### Stack
Το επόμενο βήμα ήταν να μελετήσουμε το stack.Πιο συγκεκριμένα έπρεπε να βρούμε σε ποια θέση μπαίνει το canary, που μπαίνει το return instruction address, και πόσα bytes βρίσκονται ανάμεσα στο post_data και στο canary.Για να τα βρούμε χρησιμοποιώντας gdb κάναμε δύο εκτελέσεις του pico βάζοντας breakpoint στην post_param και Content-Length = 0 στο request και χωρίς payload.
                                            
![alt text](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/img/Untitled.png)                            

΄Οπως φαίνεται και στα screenshots με την εντολή info frame βρήκαμε που αποθηκεύεται το return instruction address (0xffffcebc).Επίσης η μόνη τιμή που είχε αλλάξει στις δύο εκτελέσεις ήταν στην θέση 0xffffceac.Σε εκείνη την θέση είχαμε τρία διαφορετικά bytes και ένα 0.Έτσι βρήκαμε που μπαίνει το canary.Τέλος από το την post_data μέχρι το canary έχουμε απόσταση 15 bytes.Άρα αν βρούμε την διεύθυνση της serve_ultimate και το canary του pico τότε το payload θα είναι της μορφής 
                                            
    payload = 15 * post_data + canary + 3 * post_data + serve_ultimate address
                                            
Τις κενές θέσεις τις γεμίζουμε με την post_data επειδή θα είναι η μόνη legit δεύθυνση που θα ξέρουμε.Έτσι σε περίπτωση που άλλες μεταβλητές ( τις οποίες πατήσαμε με overflow ) πάνε να διαβαστούνε το πρόγραμμα δεν θα κρασάρει.Επίσης το Content-Length το βάζουμε ίσο με μηδέν γιατί έτσι δεν μπαίνουμε ποτέ στο loop
                                            
    // Now loop over all name=value pairs
    char* value;
    for (
      char* name = post_data;
      name < &post_data[payload_size];
      name = &value[strlen(value) + 1]      // the next name is right after the value
    ) {
      value = &name[strlen(name) + 1];      // the value is right after the name
      if (strcmp(name, param_name) == 0)
        return strdup(value);
    }
Αφού η συνθήκη 
  
    name < &post_data[payload_size];
                                    
θα είναι true.Τέλος στο canary στο μηδενικό byte δεν μπορούμε να βάλουμε απλά 0, αφού έτσι η strcpy θα σταματάει εκεί και δεν θα γράφει τίποτα πιο κάτω.Έτσι βάζουμε & το οποίο στο σημείο loop
                                    
    for (char* c = post_data; *c != '\0'; c++)
      if (*c == '&' || *c == '=')
        *c = '\0';
                      
θα μετατραπεί σε 0.
                                            
#### Printf
                                    
Τώρα που ξέρουμε πως κατασκευάζεται το payload μας μένει να βρούμε στο pico που τρέχει στο μηχάνημα που κάνουμε την επίθεση:
  - Το canary
  - Την διεύθυνση στο stack της post_data
  - Την instruction address της serve ultimate
                                    
                                    
Δυστυχώς δεν μπρούμε να τα βρούμε όπως τα βρήκαμε locally με gdb στο μηχάνημα μας.Αλλά από το 2ο ερώτημα ξέρουμε ότι μπορούμε χρησιμοποιώντας την
printf στην check auth να δούμε τιμές στην στοίβα.Άρα σαν πρώτο βήμα έπρεπε να βρούμε από ποια διεύθυνση ξεκινάει να εκτυπώνει.Για να το βρούμε αυτό κάναμε request στο pico που τρέχαμε locally και στο Authorization header βάλαμε τέσσερα %x.Βάζοντας breakpoint στην check_auth ,χρησιμοποιώντας την info frame και εκυπώνοντας την στοίβα καταφέραμε να κάνουμε match τις τιμές όπως φαίνεται στην παρακάτω εικόνα.
                                    
![alt text](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/img/210949820_1036156930483482_2030513266270692728_n.png)  
                                    
Επίσης με διαφορετικές εκτελέσεις εντοπίσαμε το canary.Άρα για να ΄κλέψουμε΄ το canary αρκεί να κάνουμε request με 27 %x ως username.Η τελευταία σημαντική πλροφορία που πήραμε είναι ότι μπορούμε να κλέψουμε από το ebp μία διεύθυνση στο stack ( με 30 %x ) και από το eip μία instruction address ( με 31 %x ).Ετσι αν βρουμε στην δικη μας εκτελεση ποσο απέχουν αυτες οι τιμές από την post_data και την διεύθυνση της serve ultimate, τότε μπορούμε να χρησιμοποιήσουμε αυτά τα offsets για να βορύμε την διεύθυνση του post_data και της serve_ultimate στο μηχάνημα που κάνουμε επίθεση.Την διεύθυνση της post_data την ξέρουμε ήδη και είναι  η 0xffffce20 ( στην πρώτη εικόνα φαίνεται 0xffffce70 και αυτό οφείλεται στο ότι κάποια screenshots βγήκαν με διαφορά ημερών από την δημιουργία του script οπότε είχαν αλλάξει οι διευθύνσεις στο stack) και στην ebp έχουμε 0xffffcf08, ενώ για την serve_ultimate με την εντολή info address serve_ultimate στο gdb παίρνουμε 0x5655689d και στην eip έχουμε 0x56556015.


### Ερώτημα 4

Για το τέταρτο ερώτημα κοιτάξαμε πάλι το pico και βρήκαμε την συνάρτηση send_file.Αυτή μας φάνηκε χρήσιμη γιατί αν την τρέχαμε θα μπορούσαμε να πάρουμε τα περιεχόμενα του var/backup/backup.log που βρήκαμε στην λύση του ερωτήματος 3.Έτσι με την ίδια λογική βρήκαμε την διεύθυνση της send_file και την βάλαμε στο payload εκεί που είχαμε βάλει την διεύθυνση της serve_ultimate στο 3ο ερώτημα.Το μόνο που έμενε ήταν το που θα βάλουμε το όνομα του αρχείου.Η send_file παίρνει ως παράμετρο το filename.Οπότε αν βάζαμε το όνομα του αρχείου που θέλαμε να ανοίξει στο post_data και με buffer_overflow πατούσαμε το filename ώστε να δείχνει στο post_data θα είμασταν έτοιμοι.
                                    
![alt text](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/img/Screenshot%202021-07-10%20at%207.34.20%20PM.png)
                                    
Στην παραπάνω εικόνα έχουμε τρέξει με gdb την send_file τοπικά.Εκεί είδαμε ότι ο ebp είναι 16 bytes μετά από το eip της post_param.Άρα καθώς δεν μπορέσαμε να βρούμε που ακριβώς βρίσκεται το filename δοκιμάσαμε να προσθέσουμε 4 φορές την διεύθυνση του post_data μετά την διεύθυνση της send_file.Το τελικό payload διαμορφώνεται ως εξής:

    payload = (file_name_aligned) + (15 - (file_name_aligned/4)) *  post_data + canary + 3 * post_data + send_file address + 4 * post_data
  
Αρχικά εμφανίσαμε το backup.log και μετά το z.log όπου βρήκαμε την λυση για το 4ο ερώτημα.

### Ερώτημα 5

Για το 5ο ερώτημα αρχικά κοιτάζοντας το 

  1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7

υποθέσαμε ότι είναι σειρά κινήσεων από σκάκι.Χρησιμοποιώντας ένα chess analysis εργαλείο βρήκαμε ότι η καλύτερη επόμενη κίνηση έιναι το c4.

![alt text](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/img/Screenshot%202021-07-13%20at%206.24.30%20PM.png)

Όσον αφορά την ip, υποθέσαμε ότι θα έπρεπε να τρέξουμε κάποια shell εντολή για να την πάρουμε.Έτσι αρχικά σκεφτήκαμε να κάνουμε χρήση της exec.Μετά από προσπάθεια, και μη έχοντας καταφέρει κάτι ζητήσαμε hint.Εκεί μας απαντήσατε ότι είμαστε σε καλό δρόμο, και να δοκιμάσουμε κάτι πιο απλό.Τελικά βρήκαμε αυτό το [άρθρο](https://css.csail.mit.edu/6.858/2011/readings/return-to-libc.pdf) που εξηγεί πως να κάνουμε return-to-libc attack, χρησιμοποιώντας την system.

Το μόνο που μας έμενε είναι να βρούμε που είναι η system στο μηχάνημα σας.Όπως αναφέρεται και στο άρθρο η system ανήκει στην βιβλιοθήκη της libc η οποία φορτώνεται σε διαφορετική θέση ανά μηχάνημα.Όμως οι συναρτήσεις της libc μεταξύ τους απέχουν πάντα το ίδιο.Άρα πάλι έπρεπε να βρούμε κάποια διεύθυνση στο μηχάνημα σας στην οποία θα προσθέταμε αυτό το offset.Αυτό το κάναμε χρησιμοποιώντας ξανά την προβληματική printf που περιγράφουμε στο 2.Σε αντίθεση με τα ερωτήματα 3 και 4, αυτήν την φορά δεν ξέραμε πόσα pops έπρεπε να κάνουμε, και δεν ξέραμε και ποια συνάρτηση ακριβώς να ψάξουμε.Αυτό το πρόβλημα το λύσαμε ως εξής.Αρχικά είδαμε που βρίσκεται η system στο μηχάνημα μας

![alt text](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/img/Screenshot%202021-07-13%20at%206.06.39%20PM.png)

Έπειτα ξέροντας ότι βρίσκεται στην θέση 0xf7b6d2e0 υποθέσαμε ότι υπόλοιπες συναρτήσεις της libc θα ξεκινάνε με κοινό πρόθεμα.'Ετσι τρέξαμε αυτό το [script](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/scripts/find_libc_function.py) το οποίο έλεγχε όλες τις τιμές που κάνει pop η printf από την θέση 1 έως 1000 και αν είχαν κοινό πρόθεμα με την system τότε εκτύπωνε την θέση που την βρήκε και την τιμή που βρήκε σε αυτήν την θέση.Τα αποτελέσματα ήταν αυτά

![alt text](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/img/Screenshot%202021-07-13%20at%206.08.00%20PM.png)

Άρα παίρνοντας το 115ο στοιχείο, υποθετικά μπορούσαμε να υπολογίσουμε το offset ( 0xf7b6d2e0 - 0xf7b48f21).Ακριβώς όπως υπολογίζαμε τις διευθύνσεις της serve_ultimate και της send_file στα προηγούμενα ερωτήματα, τώρα υπολογίζουμε της system παίρνοντας το 115ο στοιχείο και προσθέτωντας το offset που βρήκαμε.

Τέλος το payload σύμφωνα με το άρθρο και σύμφωνα με τα προηγουμένα ερωτήματα θα είναι το εξής:

  payload = 15 * post_data + canary + 3 * post_data + system_address + post_data + argument_address

Το μόνο που δεν έχουμε από τα παραπάνω είναι το argument_address το οποίο είναι ένας pointer στην εντολή που θέλουμε να εκτελεστεί από την system.Στην περίπτωση μας θέλαμε να εκτελέσουμε την "dig +short myip.opendns.com @resolver1.opendns.com", οπότε έπρεπε να την γράψουμε κάπου και μετά να δείξουμε στην θέση που την γράψαμε.Αποφασίσαμε να την γράψουμε απλά μετά το payload.Οπότε τελικά το  payload διαμορφώθηκε ως εξής:

  payload = 15 * post_data + canary + 3 * post_data + system_address + post_data + argument_address + b'dig +short myip.opendns.com @resolver1.opendns.com' 

όπου argument_address = post_data + 0x58 ( 0x58 = 88 bytes μετά την post_data)

Κάναμε το curl με το παραπάνω payload και βρήκαμε την ip 54.159.81.179.
Άρα η απάντηση στο 5 ήταν c454.159.81.179.
      
#### Script

Το [run.sh](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/scripts/run.sh) ξεκινάει ανοίγοντας tor ( 9050 ) και socat στο zwt6vcp6d5tao7tbe3je6a2q4pwdfqli62ekuhjo55c7pqlet3brutqd.onion (127.0.0.1:8000).Έπειτα εκτελεί το python script [attack_3_4_5.py](https://github.com/chatziko-ys13/2021-project-2-weaponized-assault-penguins/blob/master/scripts/attack_3_4_5.py) .Σε Δοκιμάστε επίσης να δώσετε exec δικαιώματα στο script σε περίπτωση που δεν σας τρέχει.Υπάρχουν δύο περιπτώσεις στις οποίες δεν τρέχει.Αυτές είναι:
  - αν κάποιο από τα bytes του canary,post_data,serve_ultimate_address είναι 0 ( ValueError: embedded null byte) 
  - αν έχουν " ή `.
  
Αν πέσετε σε κάποια από τις δύο περιπτώσεις θα σας προτείναμε να περιμένετε λίγο και να το ξανατρέξετε για να αλλάξουν οι τιμές των παραπάνω.   
Επίσης για να τρέχουν όλα τα ερωτήματα το ένα μετά το άλλο έχουμε βάλει timeout στο κάθε curl 3".Αν κάτι δεν προλάβει να εμφανιστεί μπορείτε να το αυξήσετε 
αλλάζοντας την τιμή μετά το flag --max-time .    


Ευχαριστούμε πολύ για το μάθημα! Καλό καλοκαίρι!
