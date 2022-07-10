vim.g.mapleader = " "
local mapper = function(mode,key,mapping)
	vim.api.nvim_set_keymap(mode, key, mapping, {noremap = true, silent = true})
end

mapper('n', '<C-s>',":w<CR>")
mapper('n', '<C-q>w',':wq<CR>')
mapper('n', '<C-q>q',':q!<CR>')
mapper('n', '<Leader>t',':t.<CR>')
mapper('n', '<Leader>n',':NvimTreeToggle<CR>')
mapper('n', '<Leader>uu',':PackerSync<CR>')
