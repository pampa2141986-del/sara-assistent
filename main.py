import json
import urllib.request
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

GEMINI_API_KEY = "AQ.Ab8RN6KnQnOj9x6Ey0puR-d_0pN1YKsrygp3is4Q1ACLI-32sg"

class SaraAssistant(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.chat_history = Label(text="SARA Assistant Ready!\n", size_hint_y=None, markup=True)
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.scroll.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll)
        
        input_box = BoxLayout(size_hint=(1, 0.2), spacing=5)
        self.user_input = TextInput(hint_text="Ask SARA anything...", multiline=False)
        self.send_btn = Button(text="Send", size_hint=(0.3, 1))
        self.send_btn.bind(on_press=self.send_message)
        
        input_box.add_widget(self.user_input)
        input_box.add_widget(self.send_btn)
        self.layout.add_widget(input_box)
        
        return self.layout

    def send_message(self, instance):
        msg = self.user_input.text.strip()
        if not msg:
            return
            
        self.chat_history.text += f"\n[b]You:[/b] {msg}\n"
        self.user_input.text = ""
        
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
            headers = {"Content-Type": "application/json"}
            data = json.dumps({"contents": [{"parts": [{"text": msg}]}]}).encode("utf-8")
            
            req = urllib.request.Request(url, data=data, headers=headers)
            with urllib.request.urlopen(req) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                reply = res_data['candidates'][0]['content']['parts'][0]['text']
                self.chat_history.text += f"[b]SARA:[/b] {reply}\n"
        except Exception:
            self.chat_history.text += "[b]SARA:[/b] Error connecting to Gemini!\n"

if __name__ == '__main__':
    SaraAssistant().run()
