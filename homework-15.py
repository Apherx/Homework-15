def errorcode(x):
    match x:
        case 500:
            print("Something went wrong in the server")
        case 401:
            print("You are not authorized to access this page")
        case 400:
            print("The server could not understand your request")
        case 403:
            print("The server understood your request,however, you are not authorized to access it")
        case 404:
            print("The page does not exist")
        case 501:
            print("The server could not understand the request method")

err = int(input("What is the error code/number? "))

(errorcode(err))

quit()