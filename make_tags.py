def make_tags(tag, word):
  tagleft = '<' + tag + '>'
  tagright = '</' + tag + '>'
  result = tagleft + word + tagright
  return result