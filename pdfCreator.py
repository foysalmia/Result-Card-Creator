from fpdf import FPDF, HTMLMixin


def pdf_generate(student):

    try:
        class MyFPDF(FPDF, HTMLMixin):
            pass

        mrk = """"""
        for j in student['marks']:
            mrk += f""" 
            <tr border="1">
                <th width="70%" align="left">{j.upper()}</th>
                <th width="30%" align="left">{student['marks'][j]}</th>
            </tr> 
            """
        html = f"""
            <font size="40" color="#042940"><p align="center"><b>RESULT CARD</b></p></font>
            <br>
            <font size="20" color="#042940"><p align="left">Name : {student['name'].upper()}</p></font>
            <font size="20" color="#042940"><p align="left">Class : {student['className']}</p></font>
            <font size="20" color="#042940"><p align="left">Roll : {student['roll']}</p></font>
            <br>
            <font size="30" color="#042940"><p align="center">Mark Sheet</p></font>
            <table border="1" align="center" width="70%">
                <thead>
                    <tr border="1">
                        <th width="70%" align="left"><h2>Subject</h2></th>
                        <th width="30%" align="left"><h2>Mark</h2></th>
                    </tr>
                </thead>
                <tbody>
                    {mrk}
                </tbody>
            </table>
            <br>
            <br>
            <font size="8" color="#808080"><i>Successfully created by <a href="https://github.com/foysalmia">Foysal Ahmed</a></i></font>
        """
        pdf = MyFPDF()
        pdf.add_page()
        pdf.write_html(html)
        pdf.output(f"{student['className']}RL{student['roll']}.pdf", 'F')
        return True
    except:
        return False
