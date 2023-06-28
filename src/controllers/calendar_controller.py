class CalendarController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames['calendar']
        self._bind()

    def _bind(self):
        pass

    def add_note(self, date, note):
        self.model.add_note(date, note)

    def get_notes(self):
        return self.model.get_notes()
    
    def edit_notes(self):
        # get selection
        notes = self.frame.table.get_selection()
        notes_id = notes['values'][2]

        # switch widgets
        self.frame.hide_widgets()
        self.frame.show_form('Edit book')
        self.frame.data_form.fill_entries(notes['values'][0:4])
        self.frame.data_form.confirm_button.configure(command=lambda: self.edit_book(notes_id))