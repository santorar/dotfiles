require('nvim-tree').setup({
  sort_by = "case_sensitive",
  view = {
    adaptive_size = true,
    mappings = {
      list = {
        { key = "u", action = "dir_up" },
      },
    },
  },
  renderer = {
    group_empty = true,
    indent_markers = {
        enable = true,
        icons = {
            corner = "└ ",
            edge = "│ ",
            item = "├ ",
            none = "  ",
        },
    },
  },
  filters = {
    dotfiles = true,
  },
  })
