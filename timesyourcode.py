import time

# ---- code you want to measure ----

start = time.perf_counter()   # place AFTER the last input statement

# ----------------------------------

end = time.perf_counter()

print(f"Elapsed time: {end - start:.10f} seconds")
