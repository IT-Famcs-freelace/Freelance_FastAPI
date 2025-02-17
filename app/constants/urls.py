from enum import Enum

class Urls(Enum):

    #auth
    login = "/login"
    logout = "/logout"
    registration = "/registration"
    verify_email = "/verify_email"
    resend_verification_code = "/resend_verification_code"
    forgot_password = "/forgot_password"
    reset_password = "/reset_password"

    #freelancers
    create_freelancer = "/freelancers/create/{id}"
    delete_freelancer = "/freelancers/delete/{id}"
    update_freelancer = "/freelancers/update/{id}"
    detail_freelancer = "/freelancers/{id}"


    #customers
    create_customer = "/customers/create/{id}"
    delete_customer = "/customers/delete/{id}"
    update_customer = "/customers/update/{id}"
    detail_customer = "/customers/{id}"

    #orders
    create_order = "/orders/create/"
    update_order = "/orders/update/{order_id}"
    detail_order = "/orders/{order_id}"
    accept_order = "/orders/accept/{order_id}"
    delete_order = "/orders/delete/{order_id}"
    close_order = "/orders/close/{order_id}"