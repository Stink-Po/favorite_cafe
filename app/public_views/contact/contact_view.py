from app.public_views import *


@app.route("/contact-us", methods=["POST", "GET"])
def contact_us():
    if request.method == "POST":
        first_name = request.form.get("fname")
        email = request.form.get("femail")
        subject = request.form.get("fsubject")
        message = request.form.get("fmessage")
        AddNewMessage(first_name=first_name,
                      email=email,
                      subject=subject,
                      message=message)
        message = "Thank You for Contacting us We Will Answer Your Message Soon as possible"
        return render_template("public/message.html",
                               user=current_user,
                               message=message)

    return render_template("public/contact.html",
                           user=current_user,
                           title="Contact us")
