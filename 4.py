import wx

class CalcFrame(wx.Frame):
    def __init__(self):
        super().__init__(
            None, title="сalculator",
            size=(300, 450))
        panel = CalcPanel(self)
        self.SetSizeHints(300, 450, 300, 450)
        self.Show()

class CalcPanel(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent)
        self.create_ui()

    def create_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        font = wx.Font(24, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.NORMAL)

        self.solution = wx.TextCtrl(self, style=wx.TE_RIGHT)
        self.solution.SetFont(font)
        self.solution.Disable()
        main_sizer.Add(self.solution, 0, wx.EXPAND|wx.ALL, 5)

        buttons = [['7', '8', '9', '/'],
                   ['4', '5', '6', '*'],
                   ['1', '2', '3', '-'],
                   ['.', '0', '⇐', '+']]
        for label_list in buttons:
            btn_sizer = wx.BoxSizer()
            for label in label_list:
                button = wx.Button(self, label=label)
                button.SetBackgroundColour((250, 250, 250, 255))
                btn_sizer.Add(button, 1, wx.EXPAND|wx.ALL)
                button.Bind(wx.EVT_BUTTON, self.update_equation)
            main_sizer.Add(btn_sizer, 1, wx.EXPAND|wx.ALL)

        equals_btn = wx.Button(self, label='=')
        equals_btn.Bind(wx.EVT_BUTTON, self.on_total)
        main_sizer.Add(equals_btn, 0, wx.EXPAND|wx.ALL, 3)

        clear_btn = wx.Button(self, label='Clear')
        clear_btn.Bind(wx.EVT_BUTTON, self.on_clear)
        main_sizer.Add(clear_btn, 0, wx.EXPAND|wx.ALL, 3)

        self.SetSizer(main_sizer)

    def update_equation(self, event):
        btn = event.GetEventObject()
        label = btn.GetLabel()
        current_equation = self.solution.GetValue()
        if label == "⇐":
            if len(current_equation)>0:
                self.solution.SetValue(current_equation[:-1])
            return
        self.solution.SetValue(current_equation + label)

    def update_solution(self):
        try:
            current_solution = str(eval(self.solution.GetValue()))
            return current_solution
        except ZeroDivisionError:
            self.solution.SetValue('ZeroDivisionError')
        except:
            pass

    def on_clear(self, event):
        self.solution.Clear()

    def on_total(self, event):
        solution = self.update_solution()
        if solution:
            self.solution.SetValue(solution)




if __name__ == '__main__':
    app = wx.App(False)
    frame = CalcFrame()
    app.MainLoop()