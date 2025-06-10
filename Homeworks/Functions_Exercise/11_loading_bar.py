def loading_bar(percent_loading):
    percent_sign_times = percent_loading / 10
    percent_sign = "%" * int(percent_sign_times)
    dot_sign = "." * (10 - int(percent_sign_times))
    message = ''
    if percent == 100:
        message = "Complete!"
        print(f"{int(percent)}% {message}")
        return f"[{percent_sign}{dot_sign}]"
    else:
        message = "Still loading..."
        print(f"{int(percent)}% [{percent_sign}{dot_sign}]")
        return message



percent = int(input())


print(loading_bar(percent))