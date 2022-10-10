class CurriculumMixin:
  def pro(self):
    msg = ""
    if hasattr(self, "previous_schools") and len(self.previous_schools) > 0: 
      msg += f"CV - Ecole : {', '.join(self.previous_schools)}"
    if hasattr(self, "previous_companies") and len(self.previous_companies) > 0: 
      msg += f"CV - Pro : {', '.join(self.previous_companies)}"
    return msg
      