from flask_restful import Resource, Api, request

from package.model import conn



class PAFH(Resource):
    """It contain all the api carryign the activity with a specific patient"""
    
    def get(self):
        """Api to retrive all the patient's past and family history from the database"""

        pafh = conn.execute("SELECT * FROM patient_history ORDER BY pat_id DESC").fetchall()
        return pafh

    #def post(self):
    """api to add the patient's past and family history in the database"""
    #patientInputPafh = request.get_json(force=True)
         
def post(self):
        """api to add the patient's past and family history in the database"""
        patientInputPafh = request.get_json(force=True)
        
       # pat_id = patientInputPafh['pat_id']
        #pat_first_name=patientInputPafh['pat_first_name']
        #pat_ph_no = patientInputPafh['pat_ph_no']
        
        #pat_age = patientInputPafh['pat_age']
        #pat_bp = patientInputPafh['pat_bp']
        
        #pat_cancer = patientInputPafh['pat_cancer']
        #pat_diabetes = patientInputPafh['pat_diabetes']
        #pat_father = patientInputPafh['pat_father']
        #pat_mother = patientInputPafh['pat_mother']
        #pat_father_age = patientInputPafh['pat_father_age']
        #pat_mother_age = patientInputPafh['pat_mother_age']
        #pat_father_bp = patientInputPafh['pat_father_bp']
        #pat_father_cancer = patientInputPafh['pat_father_cancer']
        #pat_father_diabetes = patientInputPafh['pat_father_diabetes']
        #pat_mother_bp = patientInputPafh['pat_mother_bp']
        #pat_mother_cancer = patientInputPafh['pat_mother_cancer']
        #pat_mother_diabetes = patientInputPafh['pat_mother_diabetes']

        patientInputPafh['id']=conn.execute('''INSERT INTO patient_history(id,pat_id,pat_first_name,pat_ph_no,pat_age,pat_bp,pat_cancer,pat_diabetes,pat_father,pat_mother,pat_father_age,pat_mother_age,pat_father_bp,pat_father_cancer,pat_father_diabetes,pat_mother_bp,pat_mother_cancer,pat_mother_diabetes)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', ('1','1','tejaswini','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1')).lastrowid
        conn.commit()
        return patientInputPafh
    
        #patientInputPafh['id']=conn.execute('''INSERT INTO patient_history(id,pat_id,pat_first_name,pat_ph_no,pat_age,pat_bp,pat_cancer,pat_diabetes,pat_father,pat_mother,pat_father_age,pat_mother_age,pat_father_bp,pat_father_cancer,pat_father_diabetes,pat_mother_bp,pat_mother_cancer,pat_mother_diabetes)
        #VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (pat_id,pat_first_name, pat_ph_no,pat_age,'','','','',pat_father,pat_mother,pat_father_age,pat_mother_age,'','','','','','')).lastrowid
        #conn.commit()
        #return patientInputPafh

class PAFHs(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self,id):
        """api to retrive details of the patient's past and family history by it id"""

        pafhs = conn.execute("SELECT * FROM patient_history WHERE pat_id=?",(id,)).fetchall()
        return pafhs

    #def delete(self,id):
#   """api to delete the patiend by its id"""
#
# #       conn.execute("DELETE FROM patient WHERE pat_id=?",(id,))
#     conn.commit()
    #    return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the patient by its id"""

        patientInputPafh = request.get_json(force=True)
        pat_first_name = patientInputPafh['pat_first_name']
        #pat_last_name = patientInput['pat_last_name']
        #pat_insurance_no = patientInput['pat_insurance_no']
        pat_ph_no = patientInputPafh['pat_ph_no']
        #pat_address = patientInput['pat_address']
        pat_age = patientInputPafh['pat_age']
        pat_bp = patientInputPafh['pat_bp']
        pat_cancer = patientInputPafh['pat_cancer']
        pat_diabetes = patientInputPafh['pat_diabetes']
        pat_father = patientInputPafh['pat_father']
        pat_mother = patientInputPafh['pat_mother']
        pat_father_age = patientInputPafh['pat_father_age']
        pat_mother_age = patientInputPafh['pat_mother_age']
        pat_father_bp = patientInputPafh['pat_father_bp']
        pat_father_cancer = patientInputPafh['pat_father_cancer']
        pat_father_diabetes = patientInputPafh['pat_father_diabetes']
        pat_mother_bp = patientInputPafh['pat_mother_bp']
        pat_mother_cancer = patientInputPafh['pat_mother_cancer']
        pat_mother_diabetes = patientInputPafh['pat_mother_diabetes']
        
        conn.execute("UPDATE patient_history SET pat_first_name=?,pat_ph_no=?,pat_age=?,pat_bp=?,pat_cancer=?,pat_diabetes=?,pat_father=?,pat_mother=?,pat_father_age=?,pat_mother_age=?,pat_father_bp=?,pat_father_cancer=?,pat_father_diabetes=?,pat_mother_bp=?,pat_mother_cancer=?,pat_mother_diabetes=? WHERE pat_id=?",
                     (pat_first_name,pat_ph_no,pat_age,pat_bp,pat_cancer,pat_diabetes,pat_father,pat_mother,pat_father_age,pat_mother_age,pat_father_bp,pat_father_cancer,pat_father_diabetes,pat_mother_bp,pat_mother_cancer,pat_mother_diabetes,id))
        conn.commit()
        return patientInputPafh
        
