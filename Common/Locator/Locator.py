from selenium.webdriver.common.by import By

class LocatoresClass():
    #AmazonMainPage Locators
    clickSignInSection = (By.ID, "nav-link-accountList")
    clickSignInButton = (By.ID, "ap_email")
    ContinueButton = (By.ID, "continue")
    #AmazonPasswordPage
    clickPasswordLine = (By.ID, "ap_password")
    checkBox = (By.NAME, "rememberMe")
    clickIntoSignInButton = (By.ID, "signInSubmit")
    #SearchProduct
    searchFildElement = (By.ID, "twotabsearchtextbox")
    inputProduct = (By.ID, "twotabsearchtextbox")
    clickButton = (By.ID, "nav-search-submit-button")
    #ProductFile
    clickLink = (By.XPATH, "//div[@id='search']/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div[1]/span/a/div/img")
    clickAddToCart = (By.XPATH, "//input[@id='add-to-cart-button']")
    #CartBox
    click_cart_box = (By.ID, "nav-cart")
    #ProductQuantity
    qty_button = (By.XPATH, '//span[@id="a-autoid-0-announce"]')
    increase_the_number = (By.ID, "quantity_7")
    deleteFirstProduct = (By.CLASS_NAME, "a-color-link")
    #ChangeName
    return_Account = (By.XPATH, "//a[@id='nav-link-accountList']")
    your_Account = (By.XPATH, "//div[@id='a-page']/div[2]/div/div[3]/div[3]/a/div/div")
    my_name = (By.ID, "home-profile-0")
    my_name_details = (By.ID, "name-edit-pencil-image")
    edit_section = (By.ID, "profile-name-text-input")
    save_changes = (By.CLASS_NAME, "a-button-input")
    #SignOut
    all_button = (By.ID, "nav-hamburger-menu")
    sign_out_button = (By.CLASS_NAME, "hmenu-item")




































#
# selenium Action chain
# move to
# python bulitin functions
# redirection 8 09