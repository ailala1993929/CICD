println("Hello World!")

def get_label() {
    def label = String.format("%02d",1)//格式化 字符串，不足2位的 前面补齐 0
    println "the new label is ${label}"
}

def example2() {
    println 'Hello from example2'
}
get_label()
example2()

return this