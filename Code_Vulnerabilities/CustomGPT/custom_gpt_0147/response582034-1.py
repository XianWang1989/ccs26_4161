
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable

    def __enter__(self):
        enter_loop()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        exit_loop()

    def __iter__(self):
        try:
            for item in self.loop_iterable:
                loop_start()  # Actions at the start of the loop
                yield item
                loop_end()    # Actions at the end of the loop
        finally:
            exit_loop()  # Execute cleanup when exiting the loop

# Usage of MyIterator with a context manager
with MyIterator([1, 2, 3]) as it:
    for i in it:
        print("i:", i)
        if i == 2:
            break
